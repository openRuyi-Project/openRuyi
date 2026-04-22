# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Suyun <ziyu.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global srcname jieba

Name:           python-%{srcname}
Version:        0.42.1
Release:        %autorelease
Summary:        Chinese text segmentation
License:        MIT
URL:            https://github.com/fxsjy/jieba
#!RemoteAsset:  sha256:055ca12f62674fafed09427f176506079bc135638a14e23e25be909131928db2
Source0:        https://files.pythonhosted.org/packages/source/j/%{srcname}/%{srcname}-%{version}.tar.gz
# The tarball from PyPI does not have README.md and LICENSE. So we fetch files from GitHub additionally.
#!RemoteAsset:  sha256:f7e986b6d4d067cd057b0e98a678fed7b4a76f9866571d7d65cfdada8afe4c0c
Source1:        https://raw.githubusercontent.com/fxsjy/jieba/refs/tags/v%{version}/README.md
#!RemoteAsset:  sha256:18ba0984839f85853b29fadaf992f7dba8fd0ca0fbeae34de2b8735222dc7a37
Source2:        https://raw.githubusercontent.com/fxsjy/jieba/refs/tags/v%{version}/LICENSE
BuildArch:      noarch
BuildSystem:    pyproject

BuildOption(install):  %{srcname}
# PaddlePaddle does not support riscv64.
BuildOption(check):  -e 'jieba.lac_small.*'

BuildRequires:  pyproject-rpm-macros
BuildRequires:  pkgconfig(python3)
BuildRequires:  python3dist(numpy)
BuildRequires:  python3dist(whoosh)

Provides:       python3-%{srcname} = %{version}-%{release}
%python_provide python3-%{srcname}

%description
"Jieba" (Chinese for "to stutter") Chinese text segmentation:
built to be the best Python Chinese word segmentation module.

%generate_buildrequires
%pyproject_buildrequires

%prep -a
cp %{SOURCE1} README.md
cp %{SOURCE2} LICENSE

%files -f %{pyproject_files}
%doc README.md
%license LICENSE

%changelog
%autochangelog
