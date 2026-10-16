# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Xiang W <wangxiang@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           fwupd-efi
Version:        1.8
Release:        %autorelease
Summary:        Firmware update EFI binaries
License:        LGPL-2.1-only
URL:            https://github.com/fwupd/fwupd-efi
VCS:            git@github.com:fwupd/fwupd-efi.git
#!RemoteAsset:  sha256:c9f1f9b9b967ea50eb0b478f0d7693d6673d4cd76c8e7eb80c55fc44ec928925
Source0:        https://github.com/fwupd/fwupd-efi/archive/refs/tags/%{version}.tar.gz
BuildSystem:    meson

# binutils still produces broken Optional Header (SizeOfOptionalHeader=0),
# so always use manual symbols for riscv64.
Patch2000:      2000-riscv64-pe-header-fix.patch

BuildOption(conf):  -Defi-libdir=/usr/lib64
BuildOption(conf):  -Defi_sbat_distro_id="openRuyi"
BuildOption(conf):  -Defi_sbat_distro_summary="openRuyi Creek"
BuildOption(conf):  -Defi_sbat_distro_pkgname="%{name}"
BuildOption(conf):  -Defi_sbat_distro_version="%{version}"
BuildOption(conf):  -Defi_sbat_distro_url="https://build.openruyi.cn/package/show/openruyi/%{name}"
BuildOption(conf):  -Dgenpeimg=disabled

BuildRequires:  meson
BuildRequires:  gnu-efi
BuildRequires:  python3-pefile

%description
fwupd is a project to allow updating device firmware, and this package provides
the EFI binary that is used for updating using UpdateCapsule.

%files
%doc README.md AUTHORS
%license COPYING
%{_libexecdir}/fwupd/efi/*.efi
%{_libdir}/pkgconfig/fwupd-efi.pc

%changelog
%autochangelog
