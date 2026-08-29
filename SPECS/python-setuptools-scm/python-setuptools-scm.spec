# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: Zheng Junjie <zhengjunjie@iscas.ac.cn>
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
# SPDX-FileContributor: panglars <panghao.riscv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global srcname setuptools_scm

Name:           python-setuptools-scm
Version:        10.0.5
Release:        %autorelease
Summary:        Blessed package to manage your versions by SCM tags
License:        MIT
URL:            https://github.com/pypa/setuptools-scm/
# TODO: Use %%{pypi_source %%{srcname} %%{version}} in the future - 251
#       Otherwise https://files.pythonhosted.org/packages/source/a/abc/%%{srcname}-%%{version}.tar.gz
#!RemoteAsset:  sha256:bbba8fe754516cdefd017f4456721775e6ef9662bd7887fb52ae26813d4838c3
Source0:        https://files.pythonhosted.org/packages/source/s/%{srcname}/%{srcname}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    pyproject

BuildOption(install):  setuptools_scm

BuildRequires:  pyproject-rpm-macros
BuildRequires:  pkgconfig(python3)
BuildRequires:  python3dist(setuptools) >= 77.0.3
BuildRequires:  python3dist(vcs-versioning)

Provides:       python3-setuptools-scm = %{version}-%{release}
%python_provide python3-setuptools-scm

%description
Setuptools_scm handles managing your Python package versions in SCM metadata.
It also handles file finders for the supported SCMs.

%pyproject_extras_subpkg -n python-setuptools-scm toml,rich

%prep
%autosetup -p1 -n setuptools_scm-%{version}

%generate_buildrequires
%pyproject_buildrequires

%files -f %{pyproject_files}
%doc README.md
%license LICENSE
%{_bindir}/setuptools-scm

%changelog
%autochangelog
