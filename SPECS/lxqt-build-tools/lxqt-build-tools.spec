# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: panglars <panghao.riscv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           lxqt-build-tools
Version:        2.4.0
Release:        %autorelease
Summary:        Build tools for LXQt packages
License:        BSD-3-Clause
URL:            https://lxqt-project.org/
VCS:            git:https://github.com/lxqt/lxqt-build-tools.git
#!RemoteAsset:  sha256:14999ff954e820a23af44389b9f7c65f9e58b2f1c0a559f0badd38f9b459aee6
Source0:        https://github.com/lxqt/lxqt-build-tools/releases/download/%{version}/lxqt-build-tools-%{version}.tar.xz
BuildArch:      noarch
BuildSystem:    cmake

BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  pkgconfig(Qt6Core)

Requires:       cmake
Requires:       qt6-linguist

%description
LXQt Build Tools provides tools and CMake modules used to build LXQt itself
and other components maintained by the LXQt project.

%files
%doc CHANGELOG README.md
%license BSD-3-Clause
%{_bindir}/lxqt2-transupdate
%{_datadir}/cmake/lxqt2-build-tools/

%changelog
%autochangelog
