# SPDX-FileCopyrightText: (C) 2025, 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025, 2026 openRuyi Project Contributors
# SPDX-FileContributor: Han Gao <gaohan@iscas.ac.cn>
# SPDX-FileContributor: Jingwiw <wangjingwei@iscas.ac.cn>
# SPDX-FileContributor: Zheng Junjie <zhengjunjie@iscas.ac.cn>
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0
%global modpath %{_prefix}/lib/modules/%{kver}

%ifarch riscv64
#!BuildConstraint: hardware:jobs 32
%endif

# Whether dtbs needed for arch
%ifarch riscv64
%global need_dtbs 1
%else
%global need_dtbs 0
%endif

%global signmodules 1
%global kver %{version}-%{release}
%global kernel_make_flags LD=ld.bfd KBUILD_BUILD_VERSION=%{release}

Name:           linux
Version:        7.0.9
Release:        %autorelease
Summary:        The Linux Kernel
License:        GPL-2.0-only
URL:            https://www.kernel.org/
#!RemoteAsset:  sha256:ac07acdf76cf4621cc5187a2670270a1a699533c8a6b225e4878c416ad83f1c4
Source0:        https://cdn.kernel.org/pub/linux/kernel/v7.x/linux-%{version}.tar.xz
Source1:        config.%{_arch}

BuildRequires:  gcc
BuildRequires:  bison
BuildRequires:  binutils
BuildRequires:  glibc-devel
BuildRequires:  make
BuildRequires:  perl
BuildRequires:  flex
BuildRequires:  bc
BuildRequires:  cpio
BuildRequires:  dwarves
BuildRequires:  gettext
BuildRequires:  python3
BuildRequires:  rsync
BuildRequires:  tar
BuildRequires:  xz
BuildRequires:  zstd
BuildRequires:  libdebuginfod-dummy-devel
BuildRequires:  pkgconfig(ncurses)
BuildRequires:  pkgconfig(libcap)
BuildRequires:  pkgconfig(libssh)
BuildRequires:  pkgconfig(libdw)
BuildRequires:  pkgconfig(libelf)
BuildRequires:  pkgconfig(libzstd)
BuildRequires:  pkgconfig(python3)
BuildRequires:  pkgconfig(slang)
BuildRequires:  pkgconfig(zlib)
BuildRequires:  pkgconfig(openssl)
BuildRequires:  kmod
BuildRequires:  rpm-config-openruyi

Requires:       %{name}-core%{?_isa} = %{version}-%{release}
Requires:       %{name}-modules%{?_isa} = %{version}-%{release}
%if %{need_dtbs}
Requires:       %{name}-dtbs%{?_isa} = %{version}-%{release}
%endif
Requires(post):   kmod
Requires(post):   kernel-install
Requires(postun): kernel-install

%patchlist
0001-UPSTREAM-rust-clk-implement-Send-and-Sync.patch
0002-UPSTREAM-tyr-remove-impl-Send-Sync-for-TyrData.patch
0003-UPSTREAM-pwm-th1520-remove-impl-Send-Sync-for-Th1520.patch
0004-UPSTREAM-net-spacemit-Remove-unused-buff_addr-fields.patch
0005-UPSTREAM-dt-bindings-net-Add-support-for-Spacemit-K3.patch
0006-UPSTREAM-net-stmmac-platform-Add-snps-dwmac-5.40a-IP.patch
0007-UPSTREAM-net-stmmac-Add-glue-layer-for-Spacemit-K3-S.patch
0008-UPSTREAM-drm-imagination-Improve-handling-of-unknown.patch
0009-UPSTREAM-drm-imagination-Mark-FWCCB_CMD_UPDATE_STATS.patch
0010-UPSTREAM-drm-imagination-Improve-firmware-power-off-.patch
0011-UPSTREAM-drm-imagination-Skip-2nd-thread-DM-associat.patch
0012-UPSTREAM-drm-imagination-Add-missing-rogue-context-r.patch
0013-UPSTREAM-drm-imagination-Switch-reset_reason-fields-.patch
0014-UPSTREAM-drm-imagination-Implement-handling-of-conte.patch
0015-UPSTREAM-dt-bindings-vendor-prefixes-add-verisilicon.patch
0016-UPSTREAM-dt-bindings-display-add-verisilicon-dc.patch
0017-UPSTREAM-drm-verisilicon-add-a-driver-for-Verisilico.patch
0018-UPSTREAM-dt-bindings-display-bridge-add-binding-for-.patch
0019-UPSTREAM-drm-bridge-add-a-driver-for-T-Head-TH1520-H.patch
0020-UPSTREAM-dt-bindings-mfd-spacemit-p1-Add-individual-.patch
0021-UPSTREAM-regulator-spacemit-p1-Update-supply-names.patch
0022-UPSTREAM-mmc-sdhci-of-k1-add-reset-support.patch
0023-UPSTREAM-dt-bindings-mmc-spacemit-sdhci-add-support-.patch
0024-UPSTREAM-mmc-sdhci-of-k1-spacemit-Add-support-for-K3.patch
0025-UPSTREAM-PCI-cadence-Add-flags-for-disabling-ASPM-ca.patch
0026-UPSTREAM-PCI-sg2042-Avoid-L0s-and-L1-on-Sophgo-2042-.patch
0027-UPSTREAM-dt-bindings-hwmon-moortec-mr75203-adapt-mul.patch
0028-UPSTREAM-riscv-dts-thead-add-DPU-and-HDMI-device-tre.patch
0029-UPSTREAM-riscv-dts-thead-lichee-pi-4a-enable-HDMI.patch
0030-UPSTREAM-riscv-dts-thead-th1520-add-coefficients-to-.patch
0031-UPSTREAM-riscv-dts-thead-beaglev-ahead-enable-HDMI-o.patch
0032-UPSTREAM-i2c-spacemit-move-i2c_xfer_msg.patch
0033-UPSTREAM-i2c-spacemit-introduce-pio-for-k1.patch
0034-UPSTREAM-pinctrl-spacemit-return-ENOTSUPP-for-unsupp.patch
0035-UPSTREAM-gpio-spacemit-k1-Add-set_config-callback-su.patch
0036-UPSTREAM-riscv-dts-spacemit-pcie-fix-missing-power-r.patch
0037-UPSTREAM-riscv-dts-spacemit-Update-PMIC-supply-prope.patch
0038-UPSTREAM-riscv-dts-spacemit-adapt-regulator-node-nam.patch
0039-UPSTREAM-riscv-dts-spacemit-Add-linux-pci-domain-to-.patch
0040-UPSTREAM-dt-bindings-serial-8250-spacemit-fix-clock-.patch
0041-UPSTREAM-riscv-dts-spacemit-k3-add-clock-tree.patch
0042-UPSTREAM-riscv-dts-spacemit-k3-add-pinctrl-support.patch
0043-UPSTREAM-riscv-dts-spacemit-k3-add-GPIO-support.patch
0044-UPSTREAM-riscv-dts-spacemit-k3-add-full-resource-to-.patch
0045-UPSTREAM-dt-bindings-usb-dwc3-spacemit-add-support-f.patch
0046-UPSTREAM-usb-dwc3-dwc3-generic-plat-spacemit-add-sup.patch
0047-UPSTREAM-usb-dwc3-Add-optional-VBUS-regulator-suppor.patch
0048-UPSTREAM-riscv-dts-spacemit-reorder-phy-nodes-for-K1.patch
0049-UPSTREAM-riscv-dts-spacemit-drop-incorrect-pinctrl-f.patch
0050-UPSTREAM-riscv-dts-spacemit-Add-ethernet-device-for-.patch
0051-UPSTREAM-riscv-dts-spacemit-add-LEDs-for-Milk-V-Jupi.patch
0052-UPSTREAM-riscv-dts-spacemit-add-24c04-eeprom-on-Milk.patch
0053-UPSTREAM-riscv-dts-spacemit-add-i2c-aliases-on-Milk-.patch
0054-UPSTREAM-riscv-dts-spacemit-enable-QSPI-and-add-SPI-.patch
0055-UPSTREAM-riscv-dts-spacemit-enable-USB-3-ports-on-Mi.patch
0056-UPSTREAM-riscv-dts-spacemit-enable-PCIe-ports-on-Mil.patch
0057-UPSTREAM-dt-bindings-i2c-spacemit-k3-Add-compatible.patch
0058-UPSTREAM-dts-riscv-spacemit-k3-Add-i2c-nodes.patch
0059-UPSTREAM-dts-riscv-spacemit-k3-add-P1-PMIC-regulator.patch
0060-UPSTREAM-perf-symbol-Add-RISCV-case-in-get_plt_sizes.patch
0061-UPSTREAM-clk-spacemit-ccu_mix-fix-inverted-condition.patch
0062-UPSTREAM-riscv-Simplify-assignment-for-UTS_MACHINE.patch
0063-UPSTREAM-riscv-increase-COMMAND_LINE_SIZE-value-to-2.patch
0064-UPSTREAM-riscv-acpi-update-FADT-revision-check-to-6..patch
0065-UPSTREAM-riscv-mm-WARN_ON-for-bad-addresses-in-vmemm.patch
0066-UPSTREAM-riscv-enable-HAVE_IOREMAP_PROT.patch
0067-UPSTREAM-lib-string_kunit-add-correctness-test-for-s.patch
0068-UPSTREAM-lib-string_kunit-add-correctness-test-for-s.patch
0069-UPSTREAM-lib-string_kunit-add-correctness-test-for-s.patch
0070-UPSTREAM-lib-string_kunit-add-performance-benchmark-.patch
0071-UPSTREAM-lib-string_kunit-extend-benchmarks-to-strnl.patch
0072-UPSTREAM-riscv-lib-add-strnlen-implementation.patch
0073-UPSTREAM-riscv-lib-add-strchr-implementation.patch
0074-UPSTREAM-riscv-lib-add-strrchr-implementation.patch
0075-UPSTREAM-ASoC-spacemit-move-hw-constraints-from-hw_p.patch
0076-UPSTREAM-ASoC-spacemit-adjust-FIFO-trigger-threshold.patch
0077-UPSTREAM-clk-spacemit-k3-mark-top_dclk-as-CLK_IS_CRI.patch
0078-UPSTREAM-ASoC-spacemit-fix-RX-DMA-params-not-set-whe.patch
0079-UPSTREAM-dt-bindings-usb-Add-support-for-Terminus-FE.patch
0080-UPSTREAM-usb-misc-onboard_usb_dev-Add-Terminus-FE1.1.patch
0081-UPSTREAM-iommu-riscv-Add-IOTINVAL-after-updating-DDT.patch
0082-UPSTREAM-iommu-riscv-Skip-IRQ-count-check-when-using.patch
0083-UPSTREAM-iommu-riscv-Stop-polling-when-CQCSR-reports.patch
0084-UPSTREAM-iommupt-Add-the-RISC-V-page-table-format.patch
0085-UPSTREAM-iommu-riscv-Disable-SADE.patch
0086-UPSTREAM-iommu-riscv-Use-the-generic-iommu-page-tabl.patch
0087-UPSTREAM-iommu-riscv-Enable-SVNAPOT-support-for-cont.patch
0088-UPSTREAM-iommu-riscv-Add-missing-GENERIC_MSI_IRQ.patch
0089-UPSTREAM-iommu-riscv-Allow-RISC_VIOMMU-to-COMPILE_TE.patch
0090-UPSTREAM-iommu-riscv-Fix-signedness-bug.patch
0091-UPSTREAM-iommu-riscv-Remove-overflows-on-the-invalid.patch
0092-UPSTREAM-riscv-Define-__riscv_copy_-vec_-words-bytes.patch
0093-UPSTREAM-irqchip-riscv-imsic-Clear-interrupt-move-st.patch
0094-UPSTREAM-riscv-mm-Fixup-no5lvl-failure-when-vaddr-is.patch
0095-FROMGIT-drm-imagination-Count-paired-job-fence-as-de.patch
0096-FROMGIT-drm-imagination-Fit-paired-fragment-job-in-t.patch
0097-FROMGIT-drm-imagination-Skip-check-on-paired-job-fen.patch
0098-FROMGIT-drm-imagination-Rename-pvr_queue_fence_is_uf.patch
0099-FROMGIT-drm-imagination-Rename-fence-returned-by-pvr.patch
0100-FROMGIT-drm-imagination-Move-repeated-job-fence-chec.patch
0101-FROMGIT-drm-imagination-Update-check-to-skip-prepare.patch
0102-FROMGIT-drm-imagination-Minor-improvements-to-job-su.patch
0103-FROMLIST-riscv-errata-Add-ERRATA_THEAD_WRITE_ONCE-fi.patch
0104-FROMLIST-PCI-Add-per-device-flag-to-disable-native-P.patch
0105-FROMLIST-PCI-Add-quirk-to-disable-PCIe-port-services.patch
0106-FROMLIST-PCI-Release-BAR0-of-an-integrated-bridge-to.patch
0107-BACKPORT-FROMLIST-drm-ttm-save-the-device-s-DMA-cohe.patch
0108-BACKPORT-FROMLIST-drm-ttm-downgrade-cached-to-write_.patch
0109-FROMLIST-NFU-riscv-dts-thead-Add-CPU-clock-and-OPP-t.patch
0110-FROMLIST-rust-export-BINDGEN_TARGET-from-a-separate-.patch
0111-FROMLIST-rust-generate-a-fatal-error-if-BINDGEN_TARG.patch
0112-FROMLIST-rust-add-a-Kconfig-function-to-test-for-sup.patch
0113-FROMLIST-RISC-V-handle-extension-configs-for-bindgen.patch
0114-FROMLIST-dt-bindings-mmc-spacemit-sdhci-add-reset-su.patch
0115-FROMLIST-mfd-simple-mfd-i2c-add-a-reboot-cell-for-th.patch
0116-FROMLIST-regulator-spacemit-MFD_SPACEMIT_P1-as-depen.patch
0117-FROMLIST-rtc-spacemit-default-module-when-MFD_SPACEM.patch
0118-FROMLIST-spi-dt-bindings-add-SpacemiT-K1-SPI-support.patch
0119-FROMLIST-spi-spacemit-introduce-SpacemiT-K1-SPI-cont.patch
0120-FROMLIST-riscv-dts-spacemit-define-a-SPI-controller-.patch
0121-FROMLIST-dt-bindings-thermal-Add-SpacemiT-K1-thermal.patch
0122-FROMLIST-thermal-spacemit-k1-Add-thermal-sensor-supp.patch
0123-FROMLIST-riscv-dts-spacemit-Add-thermal-sensor-for-K.patch
0124-FROMLIST-net-spacemit-Free-rings-of-memory-after-unm.patch
0125-FROMLIST-riscv-mm-Extract-helper-mark_new_valid_map.patch
0126-FROMLIST-riscv-kfence-Call-mark_new_valid_map-for-kf.patch
0127-FROMLIST-riscv-mm-Rename-new_vmalloc-into-new_valid_.patch
0128-FROMLIST-riscv-mm-Use-the-bitmap-API-for-new_valid_m.patch
0129-FROMLIST-riscv-mm-Unconditionally-sfence.vma-for-spu.patch
0130-FROMLIST-dt-bindings-phy-spacemit-k3-add-USB2-PHY-su.patch
0131-FROMLIST-phy-k1-usb-k3-add-USB2-PHY-support.patch
0132-FROMLIST-cpufreq-dt-platdev-Add-SpacemiT-K1-SoC-to-t.patch
0133-FROMLIST-riscv-dts-spacemit-Add-cpu-scaling-for-K1-S.patch
0134-FROMLIST-riscv-mm-Define-DIRECT_MAP_PHYSMEM_END.patch
0135-FROMLIST-drm-verisilicon-add-max-cursor-size-to-HWDB.patch
0136-FROMLIST-drm-verisilicon-add-support-for-cursor-plan.patch
0137-FROMLIST-riscv-add-UltraRISC-SoC-family-Kconfig-supp.patch
0138-FROMLIST-dt-bindings-PCI-Add-UltraRISC-DP1000-PCIe-c.patch
0139-FROMLIST-PCI-ultrarisc-Add-UltraRISC-DP1000-PCIe-Roo.patch
0140-FROMLIST-serial-8250_dwlib-move-DesignWare-register-.patch
0141-FROMLIST-serial-8250_dw-build-Renesas-RZN1-CPR-value.patch
0142-FROMLIST-dt-bindings-serial-snps-dw-apb-uart-Add-Ult.patch
0143-FROMLIST-serial-8250_dw-Use-a-fixed-CPR-value-for-Ul.patch
0144-FROMLIST-riscv-disable-local-interrupts-and-stop-oth.patch
0145-FROMLIST-drm-bridge-th1520-dw-hdmi-Fix-error-check-o.patch
0146-FROMLIST-drm-bridge-th1520-dw-hdmi-Fix-remove-callba.patch
0147-FROMLIST-riscv-dts-spacemit-Enable-i2c8-adapter-for-.patch
0148-FROMLIST-riscv-dts-spacemit-Define-the-P1-PMIC-regul.patch
0149-FROMLIST-riscv-dts-spacemit-Enable-USB3.0-PCIe-on-Or.patch
0150-FROMLIST-dt-bindings-dmaengine-Add-SpacemiT-K3-DMA-c.patch
0151-FROMLIST-dmaengine-mmp_pdma-refactor-DRCMR-access-wi.patch
0152-FROMLIST-dmaengine-mmp_pdma-add-SpacemiT-K3-support.patch
0153-FROMLIST-riscv-dts-spacemit-Add-PDMA-controller-node.patch
0154-FROMLIST-dt-bindings-pci-sophgo-Add-dma-coherent-pro.patch
0155-FROMLIST-riscv-dts-sophgo-Add-dma-coherent-to-SG2042.patch
0156-FROMLIST-riscv-mm-fix-SWIOTLB-initialization-for-sys.patch
0157-FROMLIST-riscv-dts-spacemit-k1-bananapi-f3-Add-vcc5v.patch
0158-FROMLIST-riscv-dts-spacemit-k1-bananapi-f3-Update-US.patch
0159-FROMLIST-riscv-dts-spacemit-k1-bananapi-f3-Correct-U.patch
0160-FROMLIST-riscv-dts-sophgo-sg2044-use-hex-for-CPU-uni.patch
0161-FROMLIST-riscv-dts-sophgo-sg2042-use-hex-for-CPU-uni.patch
0162-FROMLIST-riscv-Fix-fast_unaligned_access_speed_key-n.patch
0163-FROMLIST-riscv-dts-sophgo-reduce-SG2042-MSI-count-to.patch
0164-FROMLIST-dt-bindings-pwm-marvell-pxa-pwm-Add-Spacemi.patch
0165-FROMLIST-pwm-pxa-Add-optional-bus-clock.patch
0166-FROMLIST-riscv-ftrace-select-HAVE_BUILDTIME_MCOUNT_S.patch
0167-FROMLIST-riscv-dts-spacemit-enable-USB3-on-OrangePi-.patch
0168-FROMLIST-dts-riscv-spacemit-correct-32k-clock-freque.patch
0169-FROMLIST-ASoC-dt-bindings-add-SpacemiT-K3-SoC-compat.patch
0170-FROMLIST-ASoC-spacemit-add-K3-SoC-support-with-addit.patch
0171-FROMLIST-ASoC-soc-dai-add-shared-BCLK-clock-for-cros.patch
0172-FROMLIST-ASoC-soc-pcm-constrain-hw_params-when-DAIs-.patch
0173-FROMLIST-ASoC-spacemit-declare-shared-BCLK-for-cross.patch
0174-FROMLIST-spi-spacemit-add-u64-cast-to-NSEC_PER_SEC-t.patch
0175-FROMLIST-dt-bindings-clock-thead-add-TH1520-MISC-sub.patch
0176-FROMLIST-clk-thead-th1520-ap-add-support-for-MISC-su.patch
0177-FROMLIST-riscv-dts-thead-add-device-tree-node-for-MI.patch
0178-FROMLIST-dt-bindings-phy-add-binding-for-T-Head-TH15.patch
0179-FROMLIST-phy-add-a-driver-for-T-Head-TH1520-USB-PHY.patch
0180-FROMLIST-riscv-dts-thead-add-device-nodes-for-USB.patch
0181-FROMLIST-dt-bindings-gpio-dwapb-allow-GPIO-hogs.patch
0182-FROMLIST-dt-bindings-usb-vialab-vl817-allow-ports-pr.patch
0183-FROMLIST-riscv-dts-thead-lpi4a-sort-nodes.patch
0184-FROMLIST-riscv-dts-thead-Add-TH1520-I2C-nodes.patch
0185-FROMLIST-riscv-dts-thead-Add-Lichee-Pi-4A-IO-expansi.patch
0186-FROMLIST-riscv-dts-thead-enable-USB3-ports-on-Lichee.patch
0187-FROMLIST-riscv-dts-spacemit-k1-musepi-pro-add-PMIC-a.patch
0188-FROMLIST-riscv-dts-spacemit-k1-musepi-pro-add-24c04-.patch
0189-FROMLIST-riscv-dts-spacemit-k1-musepi-pro-enable-QSP.patch
0190-FROMLIST-riscv-dts-spacemit-k1-musepi-pro-enable-USB.patch
0191-FROMLIST-riscv-dts-spacemit-k1-musepi-pro-enable-PCI.patch
0192-FROMLIST-riscv-dts-spacemit-k1-musepi-pro-set-defaul.patch
0193-FROMLIST-riscv-dts-spacemit-k3-Add-pwm-support.patch
0194-FROMLIST-riscv-use-sysfs_emit-in-cpu_show_ghostwrite.patch
0195-FROMLIST-clk-spacemit-k3-Switch-to-pll2_d6-as-parent.patch
0196-FROMLIST-clk-spacemit-k3-Fix-PCIe-clock-register-off.patch
0197-FROMLIST-dt-bindings-soc-spacemit-k3-Add-PCIe-DBI-cl.patch
0198-FROMLIST-clk-spacemit-k3-Add-PCIe-DBI-clock.patch
0199-FROMLIST-riscv-dts-spacemit-enable-eMMC-for-OrangePi.patch
0200-FROMLIST-i2c-spacemit-configure-ILCR-IWCR-for-accura.patch
0201-FROMLIST-i2c-spacemit-drop-warning-when-clock-freque.patch
0202-FROMLIST-dt-bindings-mmc-spacemit-sdhci-add-pinctrl-.patch
0203-FROMLIST-mmc-sdhci-of-k1-enable-essential-clock-infr.patch
0204-FROMLIST-mmc-sdhci-of-k1-add-regulator-and-pinctrl-v.patch
0205-FROMLIST-mmc-sdhci-of-k1-add-comprehensive-SDR-tunin.patch
0206-FROMLIST-riscv-dts-spacemit-k1-add-SD-card-controlle.patch
0207-FROMLIST-riscv-dts-spacemit-k1-orangepi-rv2-add-SD-c.patch
0208-FROMLIST-riscv-dts-spacemit-k1-bananapi-f3-add-SD-ca.patch
0209-FROMLIST-riscv-dts-spacemit-k1-musepi-pro-add-SD-car.patch
0210-FROMLIST-riscv-dts-thead-Enable-wifi-on-the-BeagleV-.patch
0211-FROMLIST-riscv-module-Use-generic-cmp_int-instead-of.patch
0212-FROMLIST-iommu-riscv-Advertise-Svpbmt-support-to-gen.patch
0213-FROMLIST-iommupt-Encode-IOMMU_MMIO-IOMMU_CACHE-via-R.patch
0214-FROMLIST-riscv-propagate-insert_resource-result-from.patch
0215-FROMLIST-PCI-spacemit-k1-Add-device-data-support.patch
0216-FROMLIST-PCI-spacemit-k1-Add-multiple-PHY-handles-su.patch
0217-FROMLIST-dt-bindings-PCI-snps-dw-pcie-Add-msi-parent.patch
0218-FROMLIST-dt-bindings-PCI-spacemit-Introduce-Spacemit.patch
0219-FROMLIST-PCI-spacemit-k1-Add-Spacemit-K3-PCIe-host-c.patch
0220-FROMLIST-riscv-dts-spacemit-enable-QSPI-for-OrangePi.patch
0221-FROMLIST-RISC-V-KVM-Fix-NULL-pointer-dereference-in-.patch
0222-FROMLIST-clk-spacemit-k3-fix-USB2-bus-clock.patch
0223-FROMLIST-reset-spacemit-k3-fix-USB2-ahb-reset.patch
0224-FROMLIST-dts-riscv-spacemit-k3-Fix-I-O-power-setting.patch
0225-FROMLIST-riscv-dts-spacemit-set-console-baud-rate-on.patch
0226-FROMLIST-riscv-dts-spacemit-sort-aliases-on-Milk-V-J.patch
0227-FROMLIST-riscv-dts-spacemit-enable-eMMC-on-Milk-V-Ju.patch
0228-FROMLIST-riscv-dts-spacemit-enable-SD-card-support-o.patch
0229-FROMLIST-riscv-dts-spacemit-fix-uboot-partition-offs.patch
0230-FROMLIST-spi-dt-bindings-fsl-qspi-support-SpacemiT-K.patch
0231-FROMLIST-spi-fsl-qspi-add-SpacemiT-K3-support.patch
0232-FROMLIST-riscv-dts-spacemit-add-QSPI-support-for-K3-.patch
0233-FROMLIST-pinctrl-spacemit-fix-NULL-check-in-spacemit.patch
0234-FROMLIST-riscv-unconditionally-select-ARCH_KEEP_MEMB.patch
0235-FROMLIST-riscv-kexec_file-Constrain-segment-placemen.patch
0236-FROMLIST-dt-bindings-riscv-spacemit-Add-K3-CoM260-IF.patch
0237-FROMLIST-riscv-dts-spacemit-k3-Initial-support-for-C.patch
0238-FROMLIST-riscv-dts-spacemit-enable-PMIC-on-OrangePi-.patch
0239-FROMLIST-riscv-dts-spacemit-set-console-baud-rate-on.patch
0240-XUANTIE-riscv-dts-th1520-add-licheepi4a-16g-support.patch
0241-REVYOS-riscv-dts-th1520-rename-thead-to-xuantie.patch
0242-REVYOS-riscv-dts-th1520-add-xuantie-th1520-mbox-r.patch
0243-SOPHGO-dt-bindings-nvmem-Add-SG2044-eFuse-controller.patch
0244-SOPHGO-nvmem-Add-Sophgo-SG2044-eFuse-driver.patch
0245-SOPHGO-riscv-dts-sophgo-sg2044-Add-eFUSE-device.patch
0246-SOPHGO-riscv-sg2042-errata-Replace-thead-cache-clean.patch
0247-SOPHGO-dts-sg2044-Modify-pcie-bar-address.patch
0248-REVYSR-dt-bindings-net-ultrarisc-dp1000-gmac-Add-sup.patch
0249-REVYSR-net-stmmac-add-support-for-dwmac-5.10a.patch
0250-RVCK-riscv-dts-add-dp1000.dts-for-UltraRIsc-DP1000-S.patch
0251-RVCK-pinctrl-add-pinctrl-dirver-for-UltraRisc-DP1000.patch
0252-RVCK-dts-add-pinctrl-dtsi-dts-for-UltraRisc-DP1000.patch
0253-RVCK-riscv-dp1000-dts-add-the-dts-of-UltraRISC-dp100.patch
0254-RVCK-riscv-dp1000-dts-Move-mmc0-node-from-SoC-to-boa.patch
0255-RVCK-riscv-dp1000-plic-add-plic-early-init-supports.patch
0256-RVCK-riscv-dp1000-dts-Move-chosen-node-from-common-t.patch
0257-RVCK-dts-riscv-ultrarisc-Refactor-DP1000-device-tree.patch
0258-RVCK-riscv-pinctrl-ultrarisc-Implement-pin-configura.patch
0259-RVCK-riscv-dts-dp1000-add-dts-dtsi-for-Milk-V-Titan-.patch
0260-REVYSR-pinctrl-ultrarisc-cleanup-probe-remove.patch
0261-REVYSR-riscv-dp1000-dts-use-ultrarisc-dp1000-pcie-fo.patch
0262-ULTRARISC-hwmon-add-corepvt-driver-of-UltraRISC-DP10.patch
0263-RUYI-SYNC-riscv-dts-dp1000-Update-dp1000.dtsi.patch
0264-RUYI-riscv-dts-spacemit-k3-Add-USB2.0-support.patch
0265-SPACEMIT-riscv-uaccess-don-t-use-vector-if-buffer-is.patch
0266-RUYI-dt-bindings-phy-Add-Spacemit-K3-USB3-PCIe-comb-.patch
0267-RUYI-phy-spacemit-Add-USB3-PCIe-comb-PHY-driver-for-.patch
0268-RUYI-riscv-dts-spacemit-k3-add-USB-controller-and-US.patch
0269-RUYI-riscv-dts-spacemit-k3-Add-PCIe-device-node.patch
0270-RUYI-PCI-add-SpacemiT-vendor-id-and-its-K3-device-id.patch
0271-RUYI-wifi-rtw89-pci-add-SpacemiT-K3-to-36-bit-DMA-al.patch
0272-RUYI-drm-amdgpu-disable-dynamic-PCIe-speed-switch-on.patch
0273-RVCK-driver-clk-k3-keep-some-system-based-clock-alwa.patch

%description
This is a meta-package that installs the core kernel image and modules.
For a minimal boot environment, install the 'linux-core' package instead.

%package        core
Summary:        The core Linux kernel image and initrd

%description    core
Contains the bootable kernel image (vmlinuz) and a generic, pre-built initrd,
providing the minimal set of files needed to boot the system.

%package        modules
Summary:        Kernel modules for the Linux kernel
Requires:       %{name}-core = %{version}-%{release}

%description    modules
Contains all the kernel modules (.ko files) and associated metadata for
the hardware drivers and kernel features.

%package        devel
Summary:        Development files for building external kernel modules
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       dwarves

%description    devel
This package provides the kernel headers and Makefiles necessary to build
external kernel modules against the installed kernel. The development files are
located at %{_usrsrc}/kernels/%{kver}, with symlinks provided under
%{_prefix}/lib/modules/%{kver}/ for compatibility.

%if %{need_dtbs}
%package        dtbs
Summary:        Devicetree blob files from Linux sources

%description    dtbs
This package provides the DTB files built from Linux sources that may be used
for booting.
%endif

%prep
%autosetup -p1
cp %{SOURCE1} .config
echo "-%{release}" > localversion

%conf
%make_build %{kernel_make_flags} olddefconfig

%build

%make_build %{kernel_make_flags}

%if %{need_dtbs}
%make_build %{kernel_make_flags} dtbs
%endif

%install
%define ksrcpath %{buildroot}%{_usrsrc}/kernels/%{kver}
install -d %{buildroot}%{modpath} %{ksrcpath}

%make_build %{kernel_make_flags} INSTALL_MOD_PATH=%{buildroot}%{_prefix} INSTALL_MOD_STRIP=1 DEPMOD=true modules_install

%if %{need_dtbs}
%make_build %{kernel_make_flags} INSTALL_DTBS_PATH=%{buildroot}%{modpath}/dtb dtbs_install
%endif

%make_build run-command %{kernel_make_flags} KBUILD_RUN_COMMAND="$(pwd)/scripts/package/install-extmod-build %{ksrcpath}"

pushd %{buildroot}%{modpath}
rm -f build source
ln -sf %{_usrsrc}/kernels/%{kver} build
ln -sf %{_usrsrc}/kernels/%{kver} source
popd

install -Dm644 $(make %{kernel_make_flags} -s image_name) %{buildroot}%{modpath}/vmlinuz

echo "Module signing would happen here for version %{kver}."

%post
%{_bindir}/kernel-install add %{kver} %{modpath}/vmlinuz

%postun
if [ $1 -eq 0 ] ; then
    %{_bindir}/kernel-install remove %{kver}
fi

%files
%license COPYING
%doc README

%files core
%{modpath}/vmlinuz

%files modules
%{modpath}/*
%exclude %{modpath}/vmlinuz
%exclude %{modpath}/build
%exclude %{modpath}/source

%files devel
%{_usrsrc}/kernels/%{kver}/
%{modpath}/build
%{modpath}/source

%if %{need_dtbs}
%files dtbs
%{modpath}/dtb
%endif

%changelog
%autochangelog
