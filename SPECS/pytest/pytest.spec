# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: Zheng Junjie <zhengjunjie@iscas.ac.cn>
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global srcname pytest

Name:           %{srcname}
Version:        9.0.1
Release:        %autorelease
Summary:        Simple powerful testing with Python
License:        MIT
URL:            https://pytest.org
VCS:            git:https://github.com/pytest-dev/pytest
#!RemoteAsset
Source0:        https://files.pythonhosted.org/packages/source/p/%{srcname}/%{srcname}-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  pyproject-rpm-macros

Provides:       python3-%{srcname}
%python_provide python3-%{srcname}

%description
The pytest framework makes it easy to write small tests, yet scales to support
complex functional testing for applications and libraries.

%prep
%autosetup -p1

%generate_buildrequires
%pyproject_buildrequires -r

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files _pytest pytest py

mv %{buildroot}%{_bindir}/pytest %{buildroot}%{_bindir}/pytest-%{python3_version}
ln -snf pytest-%{python3_version} %{buildroot}%{_bindir}/pytest-3
mv %{buildroot}%{_bindir}/py.test %{buildroot}%{_bindir}/py.test-%{python3_version}
ln -snf py.test-%{python3_version} %{buildroot}%{_bindir}/py.test-3

# We use 3.X per default
ln -snf pytest-%{python3_version} %{buildroot}%{_bindir}/pytest
ln -snf py.test-%{python3_version} %{buildroot}%{_bindir}/py.test

# remove shebangs from all scripts
find %{buildroot}%{python3_sitelib} \
     -name '*.py' \
     -exec sed -i -e '1{/^#!/d}' {} \;

%files -f %{pyproject_files}
%{_bindir}/pytest
%{_bindir}/pytest-3
%{_bindir}/pytest-%{python3_version}
%{_bindir}/py.test
%{_bindir}/py.test-3
%{_bindir}/py.test-%{python3_version}

%changelog
%autochangelog
