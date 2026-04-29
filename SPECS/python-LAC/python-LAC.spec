# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Gui-Yue <xiangwei.riscv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global srcname LAC

Name:           python-%{srcname}
Version:        2.1.2
Release:        %autorelease
Summary:        Chinese lexical analysis toolkit by Baidu NLP
License:        Apache-2.0
URL:            https://pypi.org/project/LAC/
VCS:            git:https://github.com/baidu/lac
#!RemoteAsset:  sha256:22fcde0d5082d2044205ea6f6a7a9cd1f0d63e7b21b2dd5c9c73f27e7c0a3ef1
Source0:        https://files.pythonhosted.org/packages/source/L/%{srcname}/%{srcname}-%{version}.tar.gz
#!RemoteAsset:  sha256:559548e6f255838e4e268f9b91770bff637d63a589dbd42028fbf2f2b1e66ffd
Source1:        https://raw.githubusercontent.com/baidu/lac/e79336a5a6c0f9d583534666be6671e12958377f/LICENSE
BuildArch:      noarch
BuildSystem:    pyproject

# openRuyi-specific fix: avoid importing paddle while generating metadata/build requirements.
Patch2000:      0001-setup.py-avoid-importing-paddle-at-build-time.patch

BuildOption(install):  -l %{srcname} -L

BuildRequires:  pkgconfig(python3)
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3dist(pip)
BuildRequires:  python3dist(setuptools)
BuildRequires:  python3dist(wheel)

Provides:       python3-%{srcname} = %{version}-%{release}
%python_provide python3-%{srcname}

Requires:       python3dist(numpy)
Requires:       python3dist(paddlepaddle) >= 1.6

%description
LAC is a Chinese lexical analysis toolkit from Baidu NLP.
It provides word segmentation, POS tagging, and named entity recognition.

%prep
%autosetup -p1 -n %{srcname}-%{version}
# Upstream sdist misses LICENSE; stage it at source root for %%license.
cp %{SOURCE1} LICENSE

%generate_buildrequires
%pyproject_buildrequires

%check
# Skip runtime import checks: LAC imports paddle at runtime.

%files -f %{pyproject_files}
%doc README.md
%license LICENSE
%{_bindir}/lac

%changelog
%autochangelog
