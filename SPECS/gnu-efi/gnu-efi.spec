# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Xiang W <wangxiang@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           gnu-efi
Version:        4.0.4
Release:        %autorelease
Summary:        Building EFI Applications Using the GNU Toolchain
License:        (GPL-2.0-or-later OR BSD-3-Clause) AND BSD-3-Clause AND LGPL-2.1-or-later AND GPL-2.0-or-later AND BSD-3-Clause-Patent
URL:            https://github.com/ncroxon/gnu-efi
#!RemoteAsset:  sha256:40b61e842a4efcbf80f3e53b2f220c044e8cfe46eb4dd6396c83b751240b1c0d
Source0:        https://github.com/ncroxon/gnu-efi/archive/refs/tags/%{version}.tar.gz
BuildSystem:    autotools

BuildOption(prep):  -n %{name}-%{version}
BuildOption(build):  LD=ld.bfd PREFIX=%{_prefix} LIBDIR=%{_libdir} INSTALLROOT=%{buildroot}
BuildOption(install):  LD=ld.bfd PREFIX=%{_prefix} LIBDIR=%{_libdir} INSTALLROOT=%{buildroot}

BuildRequires:  make

%description
Building EFI Applications Using the GNU Toolchain

%conf
# No Configure

%check
# No tests

%files
%license LICENSE licenses/*
%doc README.md SECURITY.md docs/*.md
%{_includedir}/efi/*.h
%{_includedir}/efi/legacy/*.h
%{_includedir}/efi/protocol/*.h
%{_libdir}/libgnuefi.a
%{_libdir}/libefi.a
%{_libdir}/pkgconfig/gnu-efi.pc
%{_libdir}/gnuefi/apps/*.efi
%{_libdir}/gnuefi/apps/*.debug
%{_libdir}/*.lds
%{_libdir}/*.o
%ifarch x86_64
%{_includedir}/efi/x86_64/*.h
%endif
%ifarch riscv64
%{_includedir}/efi/riscv64/*.h
%endif

%changelog
%autochangelog
