# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: Zheng Junjie <zhengjunjie@iscas.ac.cn>
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global debug_package %{nil}
# The vendor name to use when installing EFI binaries.
%global _efi_vendor_ openruyi

Name:           efi-rpm-macros
Version:        5
Release:        %autorelease
Summary:        Common RPM Macros for building EFI-related packages
License:        GPL-3.0-or-later
URL:            https://github.com/rhboot/efi-rpm-macros
#!RemoteAsset
Source0:        %{url}/releases/download/%{version}/%{name}-5.tar.bz2
BuildSystem:    autotools

# https://github.com/rhboot/efi-rpm-macros/pull/3
Patch0:         0001-Add-riscv64-support.patch

BuildOption(build):  EFI_ESP_ROOT="/boot/efi"
BuildOption(build):  EFI_ARCHES="riscv64"
BuildOption(build):  EFI_VENDOR="%{_efi_vendor_}"
BuildOption(install):  EFI_ESP_ROOT="/boot/efi"
BuildOption(install):  EFI_ARCHES="riscv64"
BuildOption(install):  EFI_VENDOR="%{_efi_vendor_}"

BuildRequires:  make

%description
efi-rpm-macros provides a set of RPM macros for use in EFI-related packages.

%package     -n efi-srpm-macros
Summary:        Common SRPM Macros for building EFI-related packages
BuildArch:      noarch
Requires:       rpm

%description -n efi-srpm-macros
efi-srpm-macros provides a set of SRPM macros for use in EFI-related packages.

%package     -n efi-filesystem
Summary:        The basic directory layout for EFI machines
BuildArch:      noarch
Requires:       filesystem

%description -n efi-filesystem
The efi-filesystem package contains the basic directory layout for EFI
machine bootloaders and tools.

%conf
# No conf

%check
# no tests

%files -n efi-srpm-macros
%license LICENSE
%doc README
%{_rpmmacrodir}/macros.efi-srpm
%{_rpmconfigdir}/brp-boot-efi-times

%files -n efi-filesystem
%defattr(0700,root,root,-)
%dir /boot/efi
%dir /boot/efi/EFI
%dir /boot/efi/EFI/BOOT
%dir /boot/efi/EFI/%{_efi_vendor_}

%changelog
%autochangelog
