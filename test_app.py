from app import app

def test_header_present():
    layout = app.layout

    assert "Soul Foods Sales Visualiser" in str(layout)

def test_graph_present():
    layout = app.layout

    assert "sales-chart" in str(layout)

def test_region_picker_present():
    layout = app.layout

    assert "region-filter" in str(layout)