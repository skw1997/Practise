from src.fee_calculation.scan_operations import ScanOperations

if __name__ == '__main__':
    scan = ScanOperations()
    with scan:
        scan.global_storage_scan()