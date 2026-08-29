# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Gui-Yue <xiangwei.riscv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global srcname fontmake

Name:           python-%{srcname}
Version:        3.11.1
Release:        %autorelease
Summary:        Compile fonts from sources to OpenType and TrueType binaries
License:        Apache-2.0
URL:            https://pypi.org/project/fontmake/
VCS:            git:https://github.com/googlei18n/fontmake
#!RemoteAsset:  sha256:a3b958a2f6d0b978a803a5643f04c27c88c5ed9dc5af999752408aa94053d082
Source0:        https://files.pythonhosted.org/packages/source/f/%{srcname}/%{srcname}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    pyproject

BuildOption(install):  -l %{srcname}

BuildRequires:  pkgconfig(python3)
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3dist(pip)
BuildRequires:  python3dist(setuptools)
BuildRequires:  python3dist(wheel)

Provides:       python3-%{srcname} = %{version}-%{release}
%python_provide python3-%{srcname}

%description
Fontmake compiles fonts from source files such as UFO and Glyphs into binary
fonts, including OpenType and TrueType outputs.

%generate_buildrequires
%pyproject_buildrequires

%files -f %{pyproject_files}
%doc README.md
%license LICENSE
%{_bindir}/fontmake

%changelog
%autochangelog
