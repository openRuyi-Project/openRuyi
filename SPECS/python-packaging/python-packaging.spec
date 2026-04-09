# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: Zheng Junjie <zhengjunjie@iscas.ac.cn>
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global srcname packaging

%global flavor @BUILD_FLAVOR@%{nil}
# Set this to 1 to bootstrap.
# This mode is needed, because python3-rpm-generators need packaging
%if "%{flavor}" == "bootstrap"
%bcond bootstrap 1
%else
%bcond bootstrap 0
%endif


%if %{with bootstrap}
Name:           python-%{srcname}-bootstrap
%else
Name:           python-%{srcname}
%endif
Version:        25.0
Release:        %autorelease
Summary:        Core utilities for Python packages
License:        BSD-2-Clause OR Apache-2.0
URL:            https://github.com/pypa/packaging
#!RemoteAsset
Source:         %{url}/archive/%{version}/%{srcname}-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  pyproject-rpm-macros
BuildRequires:  unzip

%if %{with bootstrap}
BuildRequires:  python3-flit-core
%endif

%description
python-packaging provides core utilities for Python packages like utilities for
dealing with versions, specifiers, markers etc.

%package     -n python3-%{srcname}
Summary:        %{summary}
%if %{with bootstrap}
Provides:       python3dist(packaging) = %{version}
Provides:       python%{python3_version}dist(packaging) = %{version}
Requires:       python(abi) = %{python3_version}
%endif

%description -n python3-%{srcname}
python-packaging provides core utilities for Python packages like utilities for
dealing with versions, specifiers, markers etc.

%prep
%autosetup -p1 -n %{srcname}-%{version}

%if %{without bootstrap}
%generate_buildrequires
%pyproject_buildrequires -r
%endif

%build
%if %{with bootstrap}
%{python3} -m flit_core.wheel
%else
%pyproject_wheel
%endif

%install
%if %{with bootstrap}
mkdir -p %{buildroot}%{python3_sitelib}
unzip dist/packaging-%{version}-py3-none-any.whl -d %{buildroot}%{python3_sitelib} -x packaging-%{version}.dist-info/RECORD
echo '%{python3_sitelib}/packaging*' > %{pyproject_files}
%else
%pyproject_install
%pyproject_save_files %{srcname}
%endif

%files -n python3-%{srcname} -f %{pyproject_files}
%license LICENSE LICENSE.APACHE LICENSE.BSD
%doc README.rst CHANGELOG.rst CONTRIBUTING.rst

%changelog
%autochangelog
