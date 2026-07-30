from vision_pipeline.benchmark.hardware import get_cpu_name, get_gpu_name, get_total_ram

def test_get_cpu_name():
    cpu_name = get_cpu_name()
    assert isinstance(cpu_name, str)
    assert cpu_name.strip() != ""

def test_get_gpu_name():
    gpu_name = get_gpu_name()
    assert isinstance(gpu_name, str)
    assert gpu_name.strip() != ""

def test_get_total_ram():
    total_ram = get_total_ram()
    assert isinstance(total_ram, (int, float))
    assert total_ram > 0
