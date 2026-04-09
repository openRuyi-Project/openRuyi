# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
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
Version:        16.1+git20260422.c17fdb2
Release:        %autorelease
Summary:        First-stage UEFI bootloader
License:        BSD-3-Clause
URL:            https://github.com/rhboot/shim
#!RemoteAsset:  sha256:0379ce830fc34682bd66580f2be7df4154c6fabca700e75fe750cff72ffbd68c
Source0:        https://github.com/rhboot/shim/archive/c17fdb2ff23c9e28615782ac9ae268ed6a8f71f4.tar.gz
#!RemoteAsset:  sha256:40b61e842a4efcbf80f3e53b2f220c044e8cfe46eb4dd6396c83b751240b1c0d
Source1:        https://github.com/ncroxon/gnu-efi/archive/refs/tags/4.0.4.tar.gz
BuildSystem:    autotools

# https://github.com/rhboot/shim/pull/778
# The following patch is not needed.
# This is because the source code obtained by OBS is not a Git repository.
# This patch modifies Git submodules and will fail.
#Patch0001:      0001-gnu-efi-Switch-to-upstream-4.0.4-release.patch
Patch0002:      0002-Set-NO_GLIBC-1-when-building-gnu-efi.patch
Patch0003:      0003-Adopt-modern-ReallocatePool-ABI.patch
Patch0004:      0004-Adopt-modern-CompareGuid-ABI.patch
Patch0005:      0005-Correct-signedness-when-calling-string-functions.patch
Patch0006:      0006-Remove-GNU_EFI_USE_EXTERNAL_STDARG.patch
Patch0007:      0007-Avoid-misuse-of-Print-sys_va_list-funcs.patch
Patch0008:      0008-avoid-conflicting-CompareGuid.patch
Patch0009:      0009-disable-gnuefi_signed_strncmp.patch
Patch0010:      0010-fix-gnu-efi-paths.patch
Patch0011:      0011-Fix-some-lds-issues.patch
Patch0012:      0012-Initial-RISC-V-support.patch
Patch0013:      0013-bug-Remove-extraneous-configuration-from-RISC-V.patch
Patch0014:      0014-fixup-add-section-alignment-for-riscv64.patch
Patch0015:      0015-fixup-drop-va_list-related-definitions-from-stdarg.h.patch
Patch0016:      0016-Sync-elf_riscv64_efi.lds-with-gnu-efi-4.0.4.patch
Patch0017:      0017-elf_riscv64_efi.lds-Fix-section-layout-to-match-shim.patch
Patch0018:      0018-Implement-__riscv_flush_icache.patch
Patch0019:      0019-CI-Add-riscv64-cross-build-jobs.patch

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
