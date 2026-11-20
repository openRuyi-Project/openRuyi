# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%define cross_target riscv64-openruyi-linux
%define cross_sysroot %{_prefix}/%{cross_target}/sys-root

%global _lto_cflags %{nil}

Name:           cross-riscv64-binutils
Summary:        GNU Binutils for %{cross_target} cross-compilation
License:        GFDL-1.3-only AND GPL-3.0-or-later
Version:        2.46.0
Release:        %autorelease
URL:            https://www.gnu.org/software/binutils/
VCS:            git:https://sourceware.org/git/binutils-gdb.git
#!RemoteAsset:  sha256:0f3152632a2a9ce066f20963e9bb40af7cf85b9b6c409ed892fd0676e84ecd12
Source0:        https://ftp.gnu.org/gnu/binutils/binutils-%{version}.tar.bz2
BuildSystem:    autotools

# openRuyi RISC-V patches from native binutils
Patch2000:      2000-ld-riscv-data-reloc-allow-textrels-in-tests.patch
Patch2001:      2001-ld-riscv-relax-tests-accept-signed-immediates.patch
Patch2002:      2002-ld-riscv-zicfilp-accept-variable-plt-offset.patch
Patch2003:      2003-binutils-riscv-xfail-strip-annotation-symbol-tests.patch
Patch2004:      2004-ld-elf-dwarf3-accept-riscv-pie-output.patch

ExclusiveArch:  x86_64

BuildRequires:  gcc-c++
BuildRequires:  bison
BuildRequires:  flex
BuildRequires:  texinfo
BuildRequires:  zlib-ng-compat-devel
BuildRequires:  pkgconfig(libzstd)

BuildOption(build):  -C build-dir

%description
Cross-compilation binutils targeting %{cross_target}.
Provides ar, as, ld, nm, objcopy, objdump, ranlib, size, strings, strip
for the RISC-V 64-bit target with openRuyi vendor triple.

%prep
%autosetup -p1 -n binutils-%{version}

%conf
%define _configure ../configure
mkdir build-dir
cd build-dir
%configure \
    --target=%{cross_target} \
    --with-bugurl="%{_vendor_bug_url}" \
    --with-sysroot=%{cross_sysroot} \
    --with-pic \
    --with-system-zlib \
    --enable-plugins \
    --enable-threads \
    --enable-compressed-debug-sections=gas \
    --enable-new-dtags \
    --enable-default-hash-style=both \
    --enable-compressed-debug-sections=all \
    --disable-shared \
    --enable-static \
    --enable-lto \
    --disable-gprofng \
    --enable-colored-disassembly \
    --disable-werror
%undefine _configure

%install
cd build-dir
make DESTDIR=%{buildroot} install-info install
make DESTDIR=%{buildroot} install-bfd install-opcodes 2>/dev/null || true

# Save the target-specific directory and nuke everything else to avoid file
# conflicts with native binutils on the host (/usr/bin tools, host libs, etc.)
if test -d %{buildroot}/%{_prefix}/%{cross_target}; then
  cp -a %{buildroot}/%{_prefix}/%{cross_target} /tmp/_cross_binutils
fi
rm -rf %{buildroot}/*
mkdir -p %{buildroot}/%{_prefix}
mv /tmp/_cross_binutils %{buildroot}/%{_prefix}/%{cross_target}

%check
true

%files
%defattr(-,root,root)
%{_prefix}/%{cross_target}/bin/*
%{_prefix}/%{cross_target}/lib/*

%changelog
%autochangelog
