# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: Jingkun Zheng <zhengjingkun@iscas.ac.cn>
# SPDX-FileContributor: Zheng Junjie <zhengjunjie@iscas.ac.cn>
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
# SPDX-FileContributor: Xiang W <wangxiang@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

# We need to manually package debug info and sources - 251
%undefine _debuginfo_subpackages
%undefine _build_create_debug
%undefine _enable_debug_packages

# TODO: This package is NOT USABLE?

Name:           shim
Version:        16.1+git20260715.0a88e2a
Release:        %autorelease
Summary:        First-stage UEFI bootloader
License:        BSD-3-Clause
URL:            https://github.com/rhboot/shim
#!RemoteAsset:  sha256:b22f03a0eab91329fd77c14c8d9d927241336dd963b400f8df8376bb45d41b94
Source0:        https://github.com/rhboot/shim/archive/0a88e2ac01eab51a90ea61f40e0c77d619f3feab.tar.gz
#!RemoteAsset:  sha256:40b61e842a4efcbf80f3e53b2f220c044e8cfe46eb4dd6396c83b751240b1c0d
Source1:        https://github.com/ncroxon/gnu-efi/archive/refs/tags/4.0.4.tar.gz
BuildSystem:    autotools

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

%prep -a
# We use our own gnu-efi
tar --strip-components=1 -xvf %{SOURCE1} -C gnu-efi

# Force RV64GC since Zifencei is not part of RVA23U64, but RVA23S64;
# And Zifencei is part of RV64G (RV64IMAFD_Zicsr_Zifencei)
# FIXME: Forcing RV64GC is only a temporary solution.
# According to UEFI spec, we should only use `-march=rv64imac_zicsr_zifencei`, but right now this is causing FTBFS.
# See https://github.com/openRuyi-Project/openRuyi/issues/762 for more info.

%ifarch riscv64
  echo 'override CC := $(CC) -march=rv64gc' >> Make.defaults
%endif

%conf
# No Configure

%install -a
mv %{buildroot}/%{_prefix}/src/debug/%{name}* %{buildroot}/%{_prefix}/src/debug/%{name}-%{version}

%check
# No tests

%files
%defattr(-,root,root,-)
%license COPYRIGHT
%doc {BUILDING,README.{md,fallback,tpm},TODO}
%{_datadir}/shim/*
# Not sure these will be provided by this - 251
/boot/efi/EFI/BOOT/*
/boot/efi/EFI/%{_vendor}/*

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
