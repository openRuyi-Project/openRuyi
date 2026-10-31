# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Jvle <keke.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           box64
Version:        0.4.4
Release:        %autorelease
Summary:        Linux userspace x86_64 emulator
License:        MIT
URL:            https://box86.org/
VCS:            git:https://github.com/ptitSeb/box64
#!RemoteAsset:  sha256:99c6de4f509e46ab1de15df740d0e0ea338a7790efa3f67510dfbb975cc24029
Source0:        https://github.com/ptitSeb/box64/archive/refs/tags/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
ExclusiveArch:  riscv64
BuildSystem:    cmake

BuildOption(conf):  -DRV64=ON
BuildOption(conf):  -DNOGIT=ON
BuildOption(conf):  -DNO_LIB_INSTALL=ON

BuildRequires:  cmake
BuildRequires:  python3

%description
Box64 runs Linux x86_64 programs on non-x86_64 systems. On RISC-V, it uses
dynamic recompilation to translate x86_64 code for the host processor.

%package        configurator
Summary:        GTK configuration tool for Box64
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       gtk3
Requires:       python3
Requires:       python3-gobject-base

%description    configurator
Graphical GTK tool for editing Box64 configuration and browsing its options.

%check
%ctest

%files
%license LICENSE
%doc README.md
%{_bindir}/box64
%config(noreplace) /etc/binfmt.d/box64.conf
%config(noreplace) /etc/box64.box64rc

%files configurator
%{_bindir}/box64-configurator
%{_datadir}/applications/box64-configurator.desktop

%changelog
%autochangelog
