# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: Xiang W <wangxiang@iscas.ac.cn>
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
# SPDX-FileContributor: purofle <yuguo.or@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%ifarch x86_64
%define targetarch   X64
%define platformfile OvmfPkg/OvmfPkgX64.dsc
%define arch_s       64-bit x86
%endif

%ifarch riscv64
%define targetarch   RISCV64
%define platformfile OvmfPkg/RiscVVirt/RiscVVirtQemu.dsc
%define arch_s       64-bit RISC-V
%endif

Name:           ovmf
Version:        202602
Release:        %autorelease
Summary:        UEFI firmware for %{arch_s} virtual machines.
License:        BSD-2-Clause-Patent
URL:            https://github.com/tianocore/edk2
#!RemoteAsset:  git+https://github.com/tianocore/edk2.git#edk2-stable%{version}
Source0:        edk2-stable-%{version}.tar.gz

# https://github.com/tianocore/edk2/commit/a1abc3032cd271671ee3aa488725305e45a17724
Patch0:         0001-OvmfPkg-RiscVVirt-Make-SecureBootDefaultKeysInit-dri.patch

BuildRequires:  gcc
%ifarch x86_64
BuildRequires:  nasm
%endif
BuildRequires:  libuuid
BuildRequires:  util-linux
BuildRequires:  util-linux-devel
BuildRequires:  acpica
BuildRequires:  make
BuildRequires:  python3
BuildRequires:  coreutils

%description
UEFI firmware for ${arch_s} virtual machines. Open Virtual Machine Firmware
is a build of EDK II for %{arch_s} virtual machines.

%prep
%autosetup -p1 -n edk2-stable-%{version}

%build
export PACKAGES_PATH=$PWD
source edksetup.sh
make -C $EDK_TOOLS_PATH
build -t GCC -b RELEASE -a %{targetarch} -p %{platformfile} -D SECURE_BOOT_ENABLE

%install
%ifarch x86_64
install -D -m 644 Build/OvmfX64/RELEASE_GCC/FV/OVMF.fd %{buildroot}%{_datadir}/ovmf/OVMF.fd
%endif
%ifarch riscv64
truncate -s 32M Build/RiscVVirtQemu/RELEASE_GCC/FV/RISCV_VIRT_CODE.fd
truncate -s 32M Build/RiscVVirtQemu/RELEASE_GCC/FV/RISCV_VIRT_VARS.fd
install -D -m 644 Build/RiscVVirtQemu/RELEASE_GCC/FV/RISCV_VIRT_CODE.fd %{buildroot}%{_datadir}/ovmf/virt_code.fd
install -D -m 644 Build/RiscVVirtQemu/RELEASE_GCC/FV/RISCV_VIRT_VARS.fd %{buildroot}%{_datadir}/ovmf/virt_vars.fd
%endif

%files
%ifarch x86_64
%{_datadir}/ovmf/OVMF.fd
%endif
%ifarch riscv64
%{_datadir}/ovmf/virt_code.fd
%{_datadir}/ovmf/virt_vars.fd
%endif

%changelog
%autochangelog
