# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: Zheng Junjie <zhengjunjie@iscas.ac.cn>
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global srcname six

Name:           python-%{srcname}
Version:        1.17.0
Release:        %autorelease
Summary:        Python 2 and 3 compatibility utilities
License:        MIT
URL:            https://github.com/benjaminp/six
# TODO: Use %%{pypi_source %%{srcname} %%{version}} in the future - 251
#       Otherwise https://files.pythonhosted.org/packages/source/a/abc/%%{srcname}-%%{version}.tar.gz
#!RemoteAsset
Source0:        https://files.pythonhosted.org/packages/source/s/%{srcname}/%{srcname}-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  pyproject-rpm-macros
BuildRequires:  expat

%description
Six is a Python 2 and 3 compatibility library. It provides utility functions
for smoothing over the differences between the Python versions with the goal
of writing Python code that is compatible on both Python versions.

%package     -n python3-six
Summary:        %{summary}

%description -n python3-six
Six is a Python 2 and 3 compatibility library. It provides utility functions
for smoothing over the differences between the Python versions with the goal
of writing Python code that is compatible on both Python versions.

%prep
%autosetup -p1 -n six-%{version}

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files -l six

%files -n python3-six -f %{pyproject_files}
%doc README.rst documentation/index.rst

%changelog
%autochangelog
