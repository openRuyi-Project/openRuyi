# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: Zheng Junjie <zhengjunjie@iscas.ac.cn>
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global srcname setuptools_scm

Name:           python-%{srcname}
Version:        8.3.1
Release:        %autorelease
Summary:        Blessed package to manage your versions by SCM tags
License:        MIT
URL:            https://github.com/pypa/setuptools_scm/
# TODO: Use %%{pypi_source %%{srcname} %%{version}} in the future - 251
#       Otherwise https://files.pythonhosted.org/packages/source/a/abc/%%{srcname}-%%{version}.tar.gz
#!RemoteAsset
Source0:        https://files.pythonhosted.org/packages/source/s/%{srcname}/%{srcname}-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  expat

%description
Setuptools_scm handles managing your Python package versions in SCM metadata.
It also handles file finders for the supported SCMs.

%package     -n python3-setuptools_scm
Summary:        %{summary}

%description -n python3-setuptools_scm
Setuptools_scm handles managing your Python package versions in SCM metadata.
It also handles file finders for the supported SCMs.

%pyproject_extras_subpkg -n python%{python3_pkgversion}-setuptools_scm toml,rich

%prep
%autosetup -p1 -n setuptools_scm-%{version}

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files setuptools_scm

%files -n python3-setuptools_scm -f %{pyproject_files}
%doc README.md

%changelog
%autochangelog
