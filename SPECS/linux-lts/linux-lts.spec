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

%global kver %{version}-%{release}
%global kernel_make_flags LD=ld.bfd KBUILD_BUILD_VERSION=%{release}

Name:           linux-lts
Version:        6.18.28
Release:        %autorelease
Summary:        The Linux lts Kernel
License:        GPL-2.0-only
URL:            https://www.kernel.org/
#!RemoteAsset:  sha256:f360789483586cf8a20b4ab2bffe76ead6b62c0db1eeb0d917294456c4d77b74
Source0:        https://cdn.kernel.org/pub/linux/kernel/v6.x/linux-%{version}.tar.xz
Source1:        config.%{_arch}

BuildRequires:  gcc
BuildRequires:  bison
BuildRequires:  binutils
BuildRequires:  glibc-devel
BuildRequires:  make
BuildRequires:  perl
BuildRequires:  flex
BuildRequires:  bison
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
0001-UPSTREAM-drm-ttm-add-pgprot-handling-for-RISC-V.patch
0002-UPSTREAM-riscv-sophgo-dts-add-PCIe-controllers-for-S.patch
0003-UPSTREAM-riscv-sophgo-dts-enable-PCIe-for-PioneerBox.patch
0004-UPSTREAM-riscv-sophgo-dts-enable-PCIe-for-SG2042_EVB.patch
0005-UPSTREAM-riscv-sophgo-dts-enable-PCIe-for-SG2042_EVB.patch
0006-UPSTREAM-riscv-dts-sophgo-Add-SPI-NOR-node-for-SG204.patch
0007-UPSTREAM-riscv-dts-sophgo-Enable-SPI-NOR-node-for-Pi.patch
0008-UPSTREAM-riscv-dts-sophgo-Enable-SPI-NOR-node-for-SG.patch
0009-UPSTREAM-riscv-dts-sophgo-Enable-SPI-NOR-node-for-SG.patch
0010-UPSTREAM-dt-bindings-net-sophgo-sg2044-dwmac-add-phy.patch
0011-UPSTREAM-perf-vendor-events-riscv-add-T-HEAD-C920V2-.patch
0012-UPSTREAM-rust-macros-Add-support-for-imports_ns-to-m.patch
0013-UPSTREAM-pwm-Export-pwmchip_release-for-external-use.patch
0014-UPSTREAM-rust-pwm-Add-Kconfig-and-basic-data-structu.patch
0015-UPSTREAM-rust-pwm-Add-complete-abstraction-layer.patch
0016-UPSTREAM-rust-pwm-Add-module_pwm_platform_driver-mac.patch
0017-UPSTREAM-rust-pwm-Drop-wrapping-of-PWM-polarity-and-.patch
0018-UPSTREAM-rust-pwm-Fix-broken-intra-doc-link.patch
0019-UPSTREAM-pwm-Add-Rust-driver-for-T-HEAD-TH1520-SoC.patch
0020-UPSTREAM-dt-bindings-pwm-thead-Add-T-HEAD-TH1520-PWM.patch
0021-UPSTREAM-pwm-Fix-Rust-formatting.patch
0022-UPSTREAM-pwm-th1520-Fix-clippy-warning-for-redundant.patch
0023-UPSTREAM-pwm-th1520-Use-module_pwm_platform_driver-m.patch
0024-UPSTREAM-pwm-th1520-Fix-missing-Kconfig-dependencies.patch
0025-UPSTREAM-riscv-dts-thead-add-xtheadvector-to-the-th1.patch
0026-UPSTREAM-riscv-dts-thead-add-ziccrse-for-th1520.patch
0027-UPSTREAM-riscv-dts-thead-add-zfh-for-th1520.patch
0028-UPSTREAM-riscv-dts-thead-Add-PWM-controller-node.patch
0029-UPSTREAM-riscv-dts-thead-Add-PWM-fan-and-thermal-con.patch
0030-UPSTREAM-dt-bindings-vendor-prefixes-Add-UltraRISC.patch
0031-UPSTREAM-dt-bindings-interrupt-controller-Add-UltraR.patch
0032-UPSTREAM-irqchip-sifive-plic-Cache-the-interrupt-ena.patch
0033-UPSTREAM-irqchip-sifive-plic-Add-support-for-UltraRI.patch
0034-UPSTREAM-riscv-cpu_ops_sbi-smp_processor_id-returns-.patch
0035-UPSTREAM-spi-dt-bindings-fsl-qspi-support-SpacemiT-K.patch
0036-UPSTREAM-spi-dt-bindings-fsl-qspi-add-optional-reset.patch
0037-UPSTREAM-spi-fsl-qspi-add-optional-reset-support.patch
0038-UPSTREAM-spi-fsl-qspi-switch-predicates-to-bool.patch
0039-UPSTREAM-spi-fsl-qspi-add-a-clock-disable-quirk.patch
0040-UPSTREAM-spi-fsl-qspi-introduce-sfa_size-devtype-dat.patch
0041-UPSTREAM-spi-fsl-qspi-support-the-SpacemiT-K1-SoC.patch
0042-UPSTREAM-dt-bindings-pci-spacemit-Introduce-PCIe-hos.patch
0043-UPSTREAM-PCI-spacemit-Add-SpacemiT-PCIe-host-driver.patch
0044-UPSTREAM-ASoC-dt-bindings-Add-bindings-for-SpacemiT-.patch
0045-UPSTREAM-ASoC-spacemit-add-i2s-support-for-K1-SoC.patch
0046-UPSTREAM-riscv-dts-spacemit-add-UART-pinctrl-combina.patch
0047-UPSTREAM-riscv-dts-spacemit-enable-the-i2c8-adapter.patch
0048-UPSTREAM-riscv-dts-spacemit-define-fixed-regulators.patch
0049-UPSTREAM-riscv-dts-spacemit-define-regulator-constra.patch
0050-UPSTREAM-riscv-dts-spacemit-enable-the-i2c2-adapter-.patch
0051-UPSTREAM-riscv-dts-spacemit-add-24c02-eeprom-on-BPI-.patch
0052-UPSTREAM-riscv-dts-spacemit-add-i2c-aliases-on-BPI-F.patch
0053-UPSTREAM-riscv-dts-spacemit-add-Ethernet-and-PDMA-to.patch
0054-UPSTREAM-riscv-dts-spacemit-add-MusePi-Pro-board-dev.patch
0055-UPSTREAM-riscv-dts-spacemit-enable-K1-SoC-QSPI-on-BP.patch
0056-UPSTREAM-riscv-dts-spacemit-Add-OrangePi-R2S-board-d.patch
0057-UPSTREAM-riscv-dts-spacemit-reorder-i2c2-node.patch
0058-UPSTREAM-riscv-dts-spacemit-define-all-missing-I2C-c.patch
0059-UPSTREAM-rtc-spacemit-MFD_SPACEMIT_P1-as-dependencie.patch
0060-UPSTREAM-mfd-simple-mfd-i2c-Remove-select-I2C_K1-fro.patch
0061-UPSTREAM-driver-reset-spacemit-p1-add-driver-for-pow.patch
0062-UPSTREAM-riscv-remove-irqflags.h-inclusion-in-asm-bi.patch
0063-UPSTREAM-riscv-atomic.h-use-RISCV_FULL_BARRIER-in-_a.patch
0064-UPSTREAM-drm-dumb-buffers-Sanitize-output-on-errors.patch
0065-UPSTREAM-drm-dumb-buffers-Provide-helper-to-set-pitc.patch
0066-UPSTREAM-drm-vblank-Add-vblank-timer.patch
0067-UPSTREAM-drm-vblank-Add-CRTC-helpers-for-simple-use-.patch
0068-UPSTREAM-drm-vkms-Convert-to-DRM-s-vblank-timer.patch
0069-UPSTREAM-drm-hypervdrm-Use-vblank-timer.patch
0070-UPSTREAM-PCI-MSI-Convert-the-boolean-no_64bit_msi-fl.patch
0071-UPSTREAM-PCI-MSI-Check-the-device-specific-address-m.patch
0072-UPSTREAM-drm-radeon-Make-MSI-address-limit-based-on-.patch
0073-UPSTREAM-ALSA-hda-intel-Make-MSI-address-limit-based.patch
0074-UPSTREAM-riscv-dts-sophgo-enable-hardware-clock-RTC-.patch
0075-UPSTREAM-riscv-dts-sophgo-Move-PLIC-and-CLINT-node-i.patch
0076-UPSTREAM-riscv-dts-sophgo-fix-the-node-order-of-SG20.patch
0077-UPSTREAM-riscv-dts-spacemit-Enable-i2c8-adapter-for-.patch
0078-UPSTREAM-riscv-dts-spacemit-Define-fixed-regulators-.patch
0079-UPSTREAM-riscv-dts-spacemit-Define-the-P1-PMIC-regul.patch
0080-UPSTREAM-dt-bindings-phy-spacemit-Add-SpacemiT-PCIe-.patch
0081-UPSTREAM-dt-bindings-phy-spacemit-Introduce-PCIe-PHY.patch
0082-UPSTREAM-phy-spacemit-Introduce-PCIe-combo-PHY.patch
0083-UPSTREAM-riscv-dts-spacemit-Add-a-PCIe-regulator.patch
0084-UPSTREAM-riscv-dts-spacemit-PCIe-and-PHY-related-upd.patch
0085-UPSTREAM-dt-bindings-i2c-spacemit-add-optional-reset.patch
0086-UPSTREAM-i2c-k1-add-reset-support.patch
0087-UPSTREAM-riscv-dts-spacemit-add-reset-property.patch
0088-UPSTREAM-dt-bindings-phy-spacemit-add-K1-USB2-PHY.patch
0089-UPSTREAM-phy-spacemit-support-K1-USB2.0-PHY-controll.patch
0090-UPSTREAM-riscv-dts-spacemit-Add-USB2-PHY-node-for-K1.patch
0091-UPSTREAM-riscv-dts-spacemit-Add-DWC3-USB-3.0-control.patch
0092-UPSTREAM-riscv-dts-spacemit-Enable-USB3.0-on-BananaP.patch
0093-UPSTREAM-dt-bindings-pinctrl-spacemit-convert-drive-.patch
0094-UPSTREAM-dt-bindings-pinctrl-spacemit-add-K3-SoC-sup.patch
0095-UPSTREAM-pinctrl-spacemit-k3-add-initial-pin-support.patch
0096-UPSTREAM-pinctrl-spacemit-k3-adjust-drive-strength-a.patch
0097-UPSTREAM-dt-bindings-pinctrl-spacemit-add-syscon-pro.patch
0098-UPSTREAM-pinctrl-spacemit-support-I-O-power-domain-c.patch
0099-UPSTREAM-riscv-dts-spacemit-pinctrl-update-register-.patch
0100-UPSTREAM-dt-bindings-riscv-update-ratified-version-o.patch
0101-UPSTREAM-dt-bindings-riscv-Add-B-ISA-extension-descr.patch
0102-UPSTREAM-dt-bindings-riscv-Add-descriptions-for-Za64.patch
0103-UPSTREAM-dt-bindings-riscv-Add-Ssccptr-Sscounterenw-.patch
0104-UPSTREAM-dt-bindings-riscv-Add-Sha-and-its-comprised.patch
0105-UPSTREAM-riscv-dts-sophgo-sg2044-Add-b-ISA-extension.patch
0106-UPSTREAM-riscv-dts-spacemit-k1-Add-b-ISA-extension.patch
0107-UPSTREAM-dt-bindings-riscv-add-SpacemiT-X100-CPU-com.patch
0108-UPSTREAM-dt-bindings-timer-add-SpacemiT-K3-CLINT.patch
0109-UPSTREAM-dt-bindings-interrupt-controller-add-Spacem.patch
0110-UPSTREAM-dt-bindings-interrupt-controller-add-Spacem.patch
0111-UPSTREAM-dt-bindings-riscv-spacemit-add-K3-and-Pico-.patch
0112-UPSTREAM-riscv-dts-spacemit-add-initial-support-for-.patch
0113-UPSTREAM-riscv-dts-spacemit-add-K3-Pico-ITX-board-su.patch
0114-UPSTREAM-clk-spacemit-Hide-common-clock-driver-from-.patch
0115-UPSTREAM-clk-spacemit-prepare-common-ccu-header.patch
0116-UPSTREAM-clk-spacemit-extract-common-ccu-functions.patch
0117-UPSTREAM-clk-spacemit-add-platform-SoC-prefix-to-res.patch
0118-UPSTREAM-reset-spacemit-fix-auxiliary-device-id.patch
0119-UPSTREAM-dt-bindings-soc-spacemit-k3-add-clock-suppo.patch
0120-UPSTREAM-clk-spacemit-ccu_mix-add-inverted-enable-ga.patch
0121-UPSTREAM-clk-spacemit-ccu_pll-add-plla-type-clock.patch
0122-UPSTREAM-clk-spacemit-k3-extract-common-header.patch
0123-UPSTREAM-clk-spacemit-k3-add-the-clock-tree.patch
0124-UPSTREAM-dt-bindings-soc-spacemit-Add-K3-reset-suppo.patch
0125-UPSTREAM-reset-Create-subdirectory-for-SpacemiT-driv.patch
0126-UPSTREAM-reset-spacemit-Extract-common-K1-reset-code.patch
0127-UPSTREAM-reset-spacemit-Add-SpacemiT-K3-reset-driver.patch
0128-UPSTREAM-dt-bindings-gpio-spacemit-add-compatible-na.patch
0129-UPSTREAM-gpio-spacemit-Add-GPIO-support-for-K3-SoC.patch
0130-UPSTREAM-riscv-dts-spacemit-Disable-ETH-PHY-sleep-mo.patch
0131-UPSTREAM-dt-bindings-clock-thead-th1520-clk-ap-Add-I.patch
0132-UPSTREAM-clk-thead-th1520-ap-Add-C910-bus-clock.patch
0133-UPSTREAM-clk-thead-th1520-ap-Support-setting-PLL-rat.patch
0134-UPSTREAM-clk-thead-th1520-ap-Add-macro-to-define-mul.patch
0135-UPSTREAM-clk-thead-th1520-ap-Support-CPU-frequency-s.patch
0136-UPSTREAM-net-spacemit-display-phy-driver-information.patch
0137-UPSTREAM-gpio-spacemit-k1-Use-PDR-for-pin-direction-.patch
0138-UPSTREAM-phy-Kconfig-spacemit-add-COMMON_CLK-depende.patch
0139-UPSTREAM-mfd-Kconfig-Default-MFD_SPACEMIT_P1-to-m-if.patch
0140-UPSTREAM-riscv-dts-spacemit-sdhci-add-reset-support.patch
0141-UPSTREAM-irqchip-sifive-plic-Fix-call-to-__plic_togg.patch
0142-UPSTREAM-dt-bindings-interrupt-controller-sifive-pli.patch
0143-UPSTREAM-irqchip-sifive-plic-Handle-number-of-hardwa.patch
0144-UPSTREAM-PCI-dwc-Use-multiple-iATU-windows-for-mappi.patch
0145-UPSTREAM-pinctrl-th1520-Fix-typo.patch
0146-UPSTREAM-PCI-cadence-Add-module-support-for-platform.patch
0147-UPSTREAM-PCI-cadence-Split-PCIe-controller-header-fi.patch
0148-UPSTREAM-PCI-cadence-Move-PCIe-RP-common-functions-t.patch
0149-UPSTREAM-PCI-cadence-Add-support-for-High-Perf-Archi.patch
0150-UPSTREAM-net-stmmac-imx-use-phylink-s-interface-mode.patch
0151-UPSTREAM-net-stmmac-s32-move-PHY_INTF_SEL_x-definiti.patch
0152-UPSTREAM-net-stmmac-add-phy_intf_sel-and-ACTPHYIF-de.patch
0153-UPSTREAM-net-stmmac-add-stmmac_get_phy_intf_sel.patch
0154-UPSTREAM-net-stmmac-add-support-for-configuring-the-.patch
0155-UPSTREAM-net-stmmac-imx-convert-to-PHY_INTF_SEL_xxx.patch
0156-UPSTREAM-net-stmmac-imx-use-FIELD_PREP-FIELD_GET-for.patch
0157-UPSTREAM-net-stmmac-imx-use-stmmac_get_phy_intf_sel.patch
0158-UPSTREAM-net-stmmac-imx-simplify-set_intf_mode-imple.patch
0159-UPSTREAM-net-stmmac-imx-cleanup-arguments-for-set_in.patch
0160-UPSTREAM-net-stmmac-imx-use-set_phy_intf_sel.patch
0161-UPSTREAM-powerpc-pci-Initialize-msi_addr_mask-for-OF.patch
0162-UPSTREAM-sparc-PCI-Initialize-msi_addr_mask-for-OF-c.patch
0163-UPSTREAM-syscore-Pass-context-data-to-callbacks.patch
0164-UPSTREAM-irqchip-riscv-aplic-Preserve-APLIC-states-a.patch
0165-UPSTREAM-irqchip-riscv-aplic-Do-not-clear-ACPI-depen.patch
0166-UPSTREAM-irqchip-riscv-aplic-Register-syscore-operat.patch
0167-UPSTREAM-dt-bindings-usb-add-missed-compatible-strin.patch
0168-UPSTREAM-usb-dwc3-Add-software-managed-properties-fo.patch
0169-UPSTREAM-usb-dwc3-dwc3-generic-plat-Add-layerscape-d.patch
0170-UPSTREAM-dt-bindings-usb-Add-ESWIN-EIC7700-USB-contr.patch
0171-UPSTREAM-usb-dwc3-eic7700-Add-EIC7700-USB-driver.patch
0172-UPSTREAM-phy-k1-usb-add-disconnect-function-support.patch
0173-UPSTREAM-PCI-Add-ASPEED-vendor-ID-to-pci_ids.h.patch
0174-UPSTREAM-PCI-Add-PCI_BRIDGE_NO_ALIAS-quirk-for-ASPEE.patch
0175-UPSTREAM-riscv-patch-Avoid-early-phys_to_page.patch
0176-UPSTREAM-PCI-dwc-Fail-dw_pcie_host_init-if-dw_pcie_w.patch
0177-UPSTREAM-reset-spacemit-k3-Decouple-composite-reset-.patch
0178-UPSTREAM-rust-clk-implement-Send-and-Sync.patch
0179-UPSTREAM-tyr-remove-impl-Send-Sync-for-TyrData.patch
0180-UPSTREAM-pwm-th1520-fix-CLIPPY-1-warning.patch
0181-UPSTREAM-pwm-th1520-remove-impl-Send-Sync-for-Th1520.patch
0182-UPSTREAM-net-spacemit-Remove-unused-buff_addr-fields.patch
0183-UPSTREAM-dt-bindings-net-Add-support-for-Spacemit-K3.patch
0184-UPSTREAM-net-stmmac-platform-Add-snps-dwmac-5.40a-IP.patch
0185-UPSTREAM-net-stmmac-Add-glue-layer-for-Spacemit-K3-S.patch
0186-UPSTREAM-drm-imagination-Improve-handling-of-unknown.patch
0187-UPSTREAM-drm-imagination-Mark-FWCCB_CMD_UPDATE_STATS.patch
0188-UPSTREAM-drm-imagination-Improve-firmware-power-off-.patch
0189-UPSTREAM-drm-imagination-Skip-2nd-thread-DM-associat.patch
0190-UPSTREAM-drm-imagination-Add-missing-rogue-context-r.patch
0191-UPSTREAM-drm-imagination-Switch-reset_reason-fields-.patch
0192-UPSTREAM-drm-imagination-Implement-handling-of-conte.patch
0193-UPSTREAM-dt-bindings-vendor-prefixes-add-verisilicon.patch
0194-UPSTREAM-dt-bindings-display-add-verisilicon-dc.patch
0195-UPSTREAM-drm-verisilicon-add-a-driver-for-Verisilico.patch
0196-UPSTREAM-dt-bindings-display-bridge-add-binding-for-.patch
0197-UPSTREAM-drm-bridge-add-a-driver-for-T-Head-TH1520-H.patch
0198-UPSTREAM-dt-bindings-mfd-spacemit-p1-Add-individual-.patch
0199-UPSTREAM-regulator-spacemit-p1-Update-supply-names.patch
0200-UPSTREAM-mmc-sdhci-of-k1-add-reset-support.patch
0201-UPSTREAM-dt-bindings-mmc-spacemit-sdhci-add-support-.patch
0202-UPSTREAM-mmc-sdhci-of-k1-spacemit-Add-support-for-K3.patch
0203-UPSTREAM-PCI-cadence-Add-flags-for-disabling-ASPM-ca.patch
0204-UPSTREAM-PCI-sg2042-Avoid-L0s-and-L1-on-Sophgo-2042-.patch
0205-UPSTREAM-dt-bindings-hwmon-moortec-mr75203-adapt-mul.patch
0206-UPSTREAM-drm-imagination-Disable-interrupts-before-s.patch
0207-UPSTREAM-riscv-dts-thead-add-DPU-and-HDMI-device-tre.patch
0208-UPSTREAM-riscv-dts-thead-lichee-pi-4a-enable-HDMI.patch
0209-UPSTREAM-riscv-dts-thead-th1520-add-coefficients-to-.patch
0210-UPSTREAM-riscv-dts-thead-beaglev-ahead-enable-HDMI-o.patch
0211-UPSTREAM-i2c-spacemit-move-i2c_xfer_msg.patch
0212-UPSTREAM-i2c-spacemit-introduce-pio-for-k1.patch
0213-UPSTREAM-pinctrl-spacemit-return-ENOTSUPP-for-unsupp.patch
0214-UPSTREAM-gpio-spacemit-k1-Add-set_config-callback-su.patch
0215-UPSTREAM-riscv-dts-spacemit-pcie-fix-missing-power-r.patch
0216-UPSTREAM-riscv-dts-spacemit-Update-PMIC-supply-prope.patch
0217-UPSTREAM-riscv-dts-spacemit-adapt-regulator-node-nam.patch
0218-UPSTREAM-riscv-dts-spacemit-Add-linux-pci-domain-to-.patch
0219-UPSTREAM-dt-bindings-serial-8250-spacemit-fix-clock-.patch
0220-UPSTREAM-riscv-dts-spacemit-k3-add-clock-tree.patch
0221-UPSTREAM-riscv-dts-spacemit-k3-add-pinctrl-support.patch
0222-UPSTREAM-riscv-dts-spacemit-k3-add-GPIO-support.patch
0223-UPSTREAM-riscv-dts-spacemit-k3-add-full-resource-to-.patch
0224-UPSTREAM-dt-bindings-usb-dwc3-spacemit-add-support-f.patch
0225-UPSTREAM-usb-dwc3-dwc3-generic-plat-spacemit-add-sup.patch
0226-UPSTREAM-usb-dwc3-Add-optional-VBUS-regulator-suppor.patch
0227-UPSTREAM-riscv-dts-spacemit-reorder-phy-nodes-for-K1.patch
0228-UPSTREAM-riscv-dts-spacemit-drop-incorrect-pinctrl-f.patch
0229-UPSTREAM-riscv-dts-spacemit-Add-ethernet-device-for-.patch
0230-UPSTREAM-riscv-dts-spacemit-add-LEDs-for-Milk-V-Jupi.patch
0231-UPSTREAM-riscv-dts-spacemit-add-24c04-eeprom-on-Milk.patch
0232-UPSTREAM-riscv-dts-spacemit-add-i2c-aliases-on-Milk-.patch
0233-UPSTREAM-riscv-dts-spacemit-enable-QSPI-and-add-SPI-.patch
0234-UPSTREAM-riscv-dts-spacemit-enable-USB-3-ports-on-Mi.patch
0235-UPSTREAM-riscv-dts-spacemit-enable-PCIe-ports-on-Mil.patch
0236-UPSTREAM-dt-bindings-i2c-spacemit-k3-Add-compatible.patch
0237-UPSTREAM-dts-riscv-spacemit-k3-Add-i2c-nodes.patch
0238-UPSTREAM-dts-riscv-spacemit-k3-add-P1-PMIC-regulator.patch
0239-UPSTREAM-riscv-kvm-fix-vector-context-allocation-lea.patch
0240-UPSTREAM-perf-symbol-Add-RISCV-case-in-get_plt_sizes.patch
0241-UPSTREAM-clk-spacemit-ccu_mix-fix-inverted-condition.patch
0242-UPSTREAM-riscv-Simplify-assignment-for-UTS_MACHINE.patch
0243-UPSTREAM-riscv-increase-COMMAND_LINE_SIZE-value-to-2.patch
0244-UPSTREAM-riscv-acpi-update-FADT-revision-check-to-6..patch
0245-UPSTREAM-riscv-mm-WARN_ON-for-bad-addresses-in-vmemm.patch
0246-UPSTREAM-riscv-enable-HAVE_IOREMAP_PROT.patch
0247-UPSTREAM-string-provide-strends.patch
0248-UPSTREAM-lib-string_kunit-add-correctness-test-for-s.patch
0249-UPSTREAM-lib-string_kunit-add-correctness-test-for-s.patch
0250-UPSTREAM-lib-string_kunit-add-correctness-test-for-s.patch
0251-UPSTREAM-lib-string_kunit-add-performance-benchmark-.patch
0252-UPSTREAM-lib-string_kunit-extend-benchmarks-to-strnl.patch
0253-UPSTREAM-riscv-lib-add-strnlen-implementation.patch
0254-UPSTREAM-riscv-lib-add-strchr-implementation.patch
0255-UPSTREAM-riscv-lib-add-strrchr-implementation.patch
0256-UPSTREAM-PCI-dwc-Add-register-and-bitfield-definitio.patch
0257-UPSTREAM-ASoC-spacemit-move-hw-constraints-from-hw_p.patch
0258-UPSTREAM-ASoC-spacemit-adjust-FIFO-trigger-threshold.patch
0259-UPSTREAM-dt-bindings-reset-thead-th1520-reset-Remove.patch
0260-UPSTREAM-dt-bindings-reset-thead-th1520-reset-Add-co.patch
0261-UPSTREAM-reset-th1520-Prepare-for-supporting-multipl.patch
0262-UPSTREAM-reset-th1520-Support-reset-controllers-in-m.patch
0263-UPSTREAM-riscv-dts-thead-Add-reset-controllers-of-mo.patch
0264-FROMGIT-drm-imagination-Count-paired-job-fence-as-de.patch
0265-FROMGIT-drm-imagination-Fit-paired-fragment-job-in-t.patch
0266-FROMGIT-drm-imagination-Skip-check-on-paired-job-fen.patch
0267-FROMGIT-drm-imagination-Rename-pvr_queue_fence_is_uf.patch
0268-FROMGIT-drm-imagination-Rename-fence-returned-by-pvr.patch
0269-FROMGIT-drm-imagination-Move-repeated-job-fence-chec.patch
0270-FROMGIT-drm-imagination-Update-check-to-skip-prepare.patch
0271-FROMGIT-drm-imagination-Minor-improvements-to-job-su.patch
0272-FROMLIST-riscv-errata-Add-ERRATA_THEAD_WRITE_ONCE-fi.patch
0273-FROMLIST-PCI-Add-per-device-flag-to-disable-native-P.patch
0274-FROMLIST-PCI-Add-quirk-to-disable-PCIe-port-services.patch
0275-FROMLIST-PCI-Release-BAR0-of-an-integrated-bridge-to.patch
0276-BACKPORT-FROMLIST-drm-ttm-save-the-device-s-DMA-cohe.patch
0277-BACKPORT-FROMLIST-drm-ttm-downgrade-cached-to-write_.patch
0278-FROMLIST-NFU-riscv-dts-thead-Add-CPU-clock-and-OPP-t.patch
0279-FROMLIST-rust-export-BINDGEN_TARGET-from-a-separate-.patch
0280-FROMLIST-rust-generate-a-fatal-error-if-BINDGEN_TARG.patch
0281-FROMLIST-rust-add-a-Kconfig-function-to-test-for-sup.patch
0282-FROMLIST-RISC-V-handle-extension-configs-for-bindgen.patch
0283-FROMLIST-dt-bindings-mmc-spacemit-sdhci-add-reset-su.patch
0284-FROMLIST-mfd-simple-mfd-i2c-add-a-reboot-cell-for-th.patch
0285-FROMLIST-regulator-spacemit-MFD_SPACEMIT_P1-as-depen.patch
0286-FROMLIST-rtc-spacemit-default-module-when-MFD_SPACEM.patch
0287-FROMLIST-spi-dt-bindings-add-SpacemiT-K1-SPI-support.patch
0288-FROMLIST-spi-spacemit-introduce-SpacemiT-K1-SPI-cont.patch
0289-FROMLIST-riscv-dts-spacemit-define-a-SPI-controller-.patch
0290-FROMLIST-dt-bindings-thermal-Add-SpacemiT-K1-thermal.patch
0291-FROMLIST-thermal-spacemit-k1-Add-thermal-sensor-supp.patch
0292-FROMLIST-riscv-dts-spacemit-Add-thermal-sensor-for-K.patch
0293-FROMLIST-net-spacemit-Free-rings-of-memory-after-unm.patch
0294-FROMLIST-riscv-mm-Extract-helper-mark_new_valid_map.patch
0295-FROMLIST-riscv-kfence-Call-mark_new_valid_map-for-kf.patch
0296-FROMLIST-riscv-mm-Rename-new_vmalloc-into-new_valid_.patch
0297-FROMLIST-riscv-mm-Use-the-bitmap-API-for-new_valid_m.patch
0298-FROMLIST-riscv-mm-Unconditionally-sfence.vma-for-spu.patch
0299-FROMLIST-dt-bindings-phy-spacemit-k3-add-USB2-PHY-su.patch
0300-FROMLIST-phy-k1-usb-k3-add-USB2-PHY-support.patch
0301-FROMLIST-cpufreq-dt-platdev-Add-SpacemiT-K1-SoC-to-t.patch
0302-FROMLIST-riscv-dts-spacemit-Add-cpu-scaling-for-K1-S.patch
0303-FROMLIST-riscv-mm-Define-DIRECT_MAP_PHYSMEM_END.patch
0304-FROMLIST-drm-verisilicon-add-max-cursor-size-to-HWDB.patch
0305-FROMLIST-drm-verisilicon-add-support-for-cursor-plan.patch
0306-FROMLIST-riscv-add-UltraRISC-SoC-family-Kconfig-supp.patch
0307-FROMLIST-dt-bindings-PCI-Add-UltraRISC-DP1000-PCIe-c.patch
0308-FROMLIST-PCI-ultrarisc-Add-UltraRISC-DP1000-PCIe-Roo.patch
0309-FROMLIST-serial-8250_dwlib-move-DesignWare-register-.patch
0310-FROMLIST-serial-8250_dw-build-Renesas-RZN1-CPR-value.patch
0311-FROMLIST-dt-bindings-serial-snps-dw-apb-uart-Add-Ult.patch
0312-FROMLIST-serial-8250_dw-Use-a-fixed-CPR-value-for-Ul.patch
0313-FROMLIST-riscv-disable-local-interrupts-and-stop-oth.patch
0314-FROMLIST-drm-bridge-th1520-dw-hdmi-Fix-error-check-o.patch
0315-FROMLIST-drm-bridge-th1520-dw-hdmi-Fix-remove-callba.patch
0316-FROMLIST-riscv-dts-spacemit-Enable-i2c8-adapter-for-.patch
0317-FROMLIST-riscv-dts-spacemit-Define-the-P1-PMIC-regul.patch
0318-FROMLIST-riscv-dts-spacemit-Enable-USB3.0-PCIe-on-Or.patch
0319-FROMLIST-dt-bindings-dmaengine-Add-SpacemiT-K3-DMA-c.patch
0320-FROMLIST-dmaengine-mmp_pdma-support-variable-extende.patch
0321-FROMLIST-dmaengine-mmp_pdma-add-Spacemit-K3-support.patch
0322-FROMLIST-riscv-dts-spacemit-Add-PDMA-controller-node.patch
0323-FROMLIST-clk-spacemit-k3-mark-top_dclk-as-CLK_IS_CRI.patch
0324-FROMLIST-riscv-dts-spacemit-k1-musepi-pro-add-PMIC-a.patch
0325-FROMLIST-riscv-dts-spacemit-k1-musepi-pro-add-24c04-.patch
0326-FROMLIST-riscv-dts-spacemit-k1-musepi-pro-enable-QSP.patch
0327-FROMLIST-riscv-dts-spacemit-k1-musepi-pro-enable-USB.patch
0328-FROMLIST-riscv-dts-spacemit-k1-musepi-pro-enable-PCI.patch
0329-FROMLIST-riscv-dts-spacemit-k1-musepi-pro-set-defaul.patch
0330-FROMLIST-dt-bindings-mmc-spacemit-sdhci-add-pinctrl-.patch
0331-FROMLIST-mmc-sdhci-of-k1-enable-essential-clock-infr.patch
0332-FROMLIST-mmc-sdhci-of-k1-add-regulator-and-pinctrl-v.patch
0333-FROMLIST-mmc-sdhci-of-k1-add-comprehensive-SDR-tunin.patch
0334-FROMLIST-riscv-dts-spacemit-k1-add-SD-card-controlle.patch
0335-BACKPORT-FROMLIST-riscv-dts-spacemit-k1-orangepi-rv2.patch
0336-FROMLIST-riscv-dts-spacemit-k1-orangepi-rv2-add-SD-c.patch
0337-FROMLIST-riscv-dts-spacemit-k1-bananapi-f3-add-SD-ca.patch
0338-BACKPORT-FROMLIST-riscv-dts-spacemit-k1-musepi-pro-a.patch
0339-FROMLIST-dt-bindings-pci-sophgo-Add-dma-coherent-pro.patch
0340-FROMLIST-riscv-dts-sophgo-Add-dma-coherent-to-SG2042.patch
0341-FROMLIST-riscv-mm-fix-SWIOTLB-initialization-for-sys.patch
0342-FROMLIST-riscv-dts-spacemit-k1-bananapi-f3-Add-vcc5v.patch
0343-FROMLIST-riscv-dts-spacemit-k1-bananapi-f3-Update-US.patch
0344-FROMLIST-riscv-dts-spacemit-k1-bananapi-f3-Correct-U.patch
0345-FROMLIST-riscv-dts-sophgo-sg2044-use-hex-for-CPU-uni.patch
0346-FROMLIST-riscv-dts-sophgo-sg2042-use-hex-for-CPU-uni.patch
0347-FROMLIST-riscv-Fix-fast_unaligned_access_speed_key-n.patch
0348-FROMLIST-riscv-Define-__riscv_copy_-vec_-words-bytes.patch
0349-FROMLIST-riscv-dts-sophgo-reduce-SG2042-MSI-count-to.patch
0350-FROMLIST-dt-bindings-pwm-marvell-pxa-pwm-Add-Spacemi.patch
0351-FROMLIST-pwm-pxa-Add-optional-bus-clock.patch
0352-FROMLIST-riscv-ftrace-select-HAVE_BUILDTIME_MCOUNT_S.patch
0353-FROMLIST-riscv-dts-spacemit-add-fixed-regulators-for.patch
0354-FROMLIST-riscv-dts-spacemit-enable-USB3-on-OrangePi-.patch
0355-FROMLIST-riscv-mm-Fixup-no5lvl-failure-when-vaddr-is.patch
0356-FROMLIST-dts-riscv-spacemit-correct-32k-clock-freque.patch
0357-FROMLIST-ASoC-spacemit-fix-RX-DMA-params-not-set-whe.patch
0358-FROMLIST-ASoC-dt-bindings-add-SpacemiT-K3-SoC-compat.patch
0359-FROMLIST-ASoC-spacemit-add-K3-SoC-support-with-addit.patch
0360-FROMLIST-ASoC-soc-dai-add-shared-BCLK-clock-for-cros.patch
0361-FROMLIST-ASoC-soc-pcm-constrain-hw_params-when-DAIs-.patch
0362-FROMLIST-ASoC-spacemit-declare-shared-BCLK-for-cross.patch
0363-FROMLIST-dt-bindings-phy-Add-Spacemit-K3-USB3-PCIe-c.patch
0364-FROMLIST-phy-spacemit-Add-USB3-PCIe-comb-PHY-driver-.patch
0365-FROMLIST-PCI-spacemit-k1-Add-device-data-support.patch
0366-FROMLIST-PCI-spacemit-k1-Add-multiple-phy-handles-su.patch
0367-FROMLIST-dt-bindings-PCI-snps-dw-pcie-Add-msi-parent.patch
0368-FROMLIST-dt-bindings-pci-spacemit-Introduce-Spacemit.patch
0369-FROMLIST-PCI-spacemit-k1-Add-Spacemit-K3-PCIe-host-c.patch
0370-FROMLIST-irqchip-riscv-imsic-sync-up-state-before-CP.patch
0371-FROMLIST-spi-spacemit-add-u64-cast-to-NSEC_PER_SEC-t.patch
0372-FROMLIST-dt-bindings-clock-thead-add-TH1520-MISC-sub.patch
0373-FROMLIST-clk-thead-th1520-ap-add-support-for-MISC-su.patch
0374-FROMLIST-riscv-dts-thead-add-device-tree-node-for-MI.patch
0375-FROMLIST-dt-bindings-phy-add-binding-for-T-Head-TH15.patch
0376-FROMLIST-phy-add-a-driver-for-T-Head-TH1520-USB-PHY.patch
0377-FROMLIST-riscv-dts-thead-add-device-nodes-for-USB.patch
0378-FROMLIST-dt-bindings-gpio-dwapb-allow-GPIO-hogs.patch
0379-FROMLIST-dt-bindings-usb-vialab-vl817-allow-ports-pr.patch
0380-FROMLIST-riscv-dts-thead-lpi4a-sort-nodes.patch
0381-FROMLIST-riscv-dts-thead-Add-TH1520-I2C-nodes.patch
0382-FROMLIST-riscv-dts-thead-Add-Lichee-Pi-4A-IO-expansi.patch
0383-FROMLIST-riscv-dts-thead-enable-USB3-ports-on-Lichee.patch
0384-FROMLIST-rxrpc-Also-unshare-DATA-RESPONSE-packets-wh.patch
0385-XUANTIE-riscv-dts-th1520-add-licheepi4a-16g-support.patch
0386-REVYOS-riscv-dts-th1520-rename-thead-to-xuantie.patch
0387-REVYOS-riscv-dts-th1520-add-xuantie-th1520-mbox-r.patch
0388-SOPHGO-dt-bindings-nvmem-Add-SG2044-eFuse-controller.patch
0389-SOPHGO-nvmem-Add-Sophgo-SG2044-eFuse-driver.patch
0390-SOPHGO-riscv-dts-sophgo-sg2044-Add-eFUSE-device.patch
0391-SOPHGO-dts-sg2044-Modify-pcie-bar-address.patch
0392-SOPHGO-riscv-sg2042-errata-Replace-thead-cache-clean.patch
0393-REVYSR-dt-bindings-net-ultrarisc-dp1000-gmac-Add-sup.patch
0394-REVYSR-net-stmmac-add-support-for-dwmac-5.10a.patch
0395-RVCK-riscv-dts-add-dp1000.dts-for-UltraRIsc-DP1000-S.patch
0396-RVCK-pinctrl-add-pinctrl-dirver-for-UltraRisc-DP1000.patch
0397-RVCK-dts-add-pinctrl-dtsi-dts-for-UltraRisc-DP1000.patch
0398-RVCK-riscv-dp1000-dts-add-the-dts-of-UltraRISC-dp100.patch
0399-RVCK-riscv-dp1000-dts-Move-mmc0-node-from-SoC-to-boa.patch
0400-RVCK-riscv-dp1000-plic-add-plic-early-init-supports.patch
0401-RVCK-riscv-dp1000-dts-Move-chosen-node-from-common-t.patch
0402-RVCK-dts-riscv-ultrarisc-Refactor-DP1000-device-tree.patch
0403-RVCK-riscv-pinctrl-ultrarisc-Implement-pin-configura.patch
0404-RVCK-riscv-dts-dp1000-add-dts-dtsi-for-Milk-V-Titan-.patch
0405-REVYSR-pinctrl-ultrarisc-cleanup-probe-remove.patch
0406-REVYSR-riscv-dp1000-dts-use-ultrarisc-dp1000-pcie-fo.patch
0407-ULTRARISC-hwmon-add-corepvt-driver-of-UltraRISC-DP10.patch
0408-RUYI-SYNC-riscv-dts-dp1000-Update-dp1000.dtsi.patch

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
%autosetup -p1 -n linux-%{version}
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
