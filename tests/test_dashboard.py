from pathlib import Path
import hashlib
import sys
import unittest

from streamlit.testing.v1 import AppTest

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
from common.dashboard_app import load_all_team_reports, load_reports


class DashboardTest(unittest.TestCase):
    def test_scope_and_history(self):
        self.assertEqual({p.name for p in (ROOT / 'teams').iterdir() if p.is_dir()}, {'t2'})
        reports = load_reports(ROOT / 'teams/t2/data/relatos', 'T2')
        self.assertEqual([r.sprint for r in reports], ['Sprint 0', 'Sprint 1', 'Sprint 3'])
        self.assertEqual(len(load_all_team_reports(ROOT / 'teams/t2')), 3)
        hashes = {
            0: 'c61b0a4721f9114630226a04a7b20d845eea4e5f0679a03f17b97e6c32ae4803',
            1: '3439989ed53f97c9e8e5d12c4659d5b035706a363f8c45befeaa6a706512fa0f',
        }
        for sprint, expected in hashes.items():
            path = ROOT / f'teams/t2/data/relatos/relato_Sprint_{sprint}_-_Survey_Alunos_{sprint}_-_T2.md'
            self.assertEqual(hashlib.sha256(path.read_bytes()).hexdigest(), expected)

    def test_current_values(self):
        current = load_reports(ROOT / 'teams/t2/data/relatos', 'T2')[-1]
        self.assertEqual(current.participation, '4/6 (66.7%)')
        self.assertAlmostEqual(current.overall, 7.149305555555555, delta=.005)
        self.assertEqual(len(current.space), 4)
        self.assertEqual(len(current.top5), 5)
        self.assertEqual(len(current.bottom5), 5)
        self.assertTrue(any('2 respostas v\u00e1lidas' in label and score == 2.5 for label, score in current.bottom5))

    def test_app_and_filters(self):
        app = AppTest.from_file(str(ROOT / 'teams/t2/app.py'), default_timeout=30).run()
        self.assertFalse(app.exception)
        self.assertIn('T2', app.title[0].value)
        self.assertEqual(app.sidebar.multiselect[0].value, ['Sprint 0', 'Sprint 1', 'Sprint 3'])
        self.assertEqual(len(app.get('plotly_chart')), 3)
        self.assertTrue(any('pelo menos duas equipes' in info.value for info in app.info))
        self.assertTrue(any('Sprint 2' in caption.value and 'nao significa zero' in caption.value for caption in app.caption))
        app.sidebar.multiselect[0].set_value(['Sprint 3']).run()
        self.assertFalse(app.exception)
        self.assertTrue(any(m.label == 'Nota do Survey' and m.value == '7.15' for m in app.metric))
        app.sidebar.multiselect[1].set_value(['SPACE-P (Performance)']).run()
        self.assertFalse(app.exception)
        self.assertTrue(any(m.label == 'M\u00e9dia SPACE filtrada' and m.value == '5.94' for m in app.metric))


if __name__ == '__main__':
    unittest.main()
