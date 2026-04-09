# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: Zheng Junjie <zhengjunjie@iscas.ac.cn>
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

# We need to manually package debug info and sources - 251
%undefine _debuginfo_subpackages
%undefine _build_create_debug
%undefine _enable_debug_packages

# TODO: This package is NOT USABLE?

Name:           shim
Version:        16.1
Release:        %autorelease
Summary:        First-stage UEFI bootloader
License:        BSD-3-Clause
URL:            https://github.com/rhboot/shim
#!RemoteAsset:  git+https://github.com/rhboot/shim.git#16.1
#!CreateArchive
Source0:        shim.tar.gz
#!RemoteAsset:  git+https://github.com/ncroxon/gnu-efi.git#ee80edbb57331968c541903762cb65280fe23a6f
#!CreateArchive
Source1:        gnu-efi.tar.gz
BuildSystem:    autotools

# https://github.com/rhboot/shim/pull/778
Patch0:         0001-add-riscv64-support.patch

BuildOption(build):  EFIDIR=%{_vendor} LD=ld.bfd
BuildOption(install):  DATATARGETDIR="%{_datadir}/shim" EFIDIR=%{_vendor} install-as-data

BuildRequires:  efi-filesystem
BuildRequires:  efi-srpm-macros
BuildRequires:  pkgconfig(libelf)
BuildRequires:  make
# This is a placeholder requires, we don't actually use it now - 251
BuildRequires:  pesign

%description
Initial UEFI bootloader that handles chaining to a trusted full bootloader
under secure boot environments. This package contains the version signed by
the UEFI signing service.

%package        debuginfo
Summary:        UEFI shim loader - debug symbols

%description    debuginfo
The debug symbols of UEFI shim loader

%package        debugsource
Summary:        UEFI shim loader - debug source

%description    debugsource
The source code of UEFI shim loader

%prep
%setup -q -n %{name}

# We use our own gnu-efi
rm -rf gnu-efi
tar xf %{SOURCE1}
# Hey, we can't patch a submodule folder, so this... - 251
%{__patch} -p1 -F3 -l --no-backup-if-mismatch < %{PATCH0} || true

sed -e 's/-Werror\b//g' -i Makefile Make.defaults

%conf
# No Configure

%install -a

%files
%defattr(-,root,root,-)
%license COPYRIGHT
%doc {BUILDING,README.{md,fallback,tpm},TODO}
%{_datadir}/shim/*
# Not sure these will be provided by this - 251
/boot/efi/EFI/BOOT/*
/boot/efi/EFI/%{_vendor}/*

# No tests
%check

%files debuginfo
%defattr(-,root,root,-)
%ifarch x86_64
%{_prefix}/lib/debug/boot/efi/EFI/%{_vendor}/fbx64.efi.debug
%{_prefix}/lib/debug/boot/efi/EFI/%{_vendor}/mmx64.efi.debug
%{_prefix}/lib/debug/boot/efi/EFI/%{_vendor}/shimx64.efi.debug
%endif
%ifarch riscv64
%{_prefix}/lib/debug/boot/efi/EFI/%{_vendor}/fbriscv64.efi.debug
%{_prefix}/lib/debug/boot/efi/EFI/%{_vendor}/mmriscv64.efi.debug
%{_prefix}/lib/debug/boot/efi/EFI/%{_vendor}/shimriscv64.efi.debug
%endif
# Uh... What the hell - 251
%dir %{_prefix}/lib/debug/.build-id
%{_prefix}/lib/debug/.build-id/*/*

%files debugsource
%defattr(-,root,root,-)
%dir %{_prefix}/src/debug/%{name}-%{version}
%{_prefix}/src/debug/%{name}-%{version}/*

%changelog
%autochangelog
