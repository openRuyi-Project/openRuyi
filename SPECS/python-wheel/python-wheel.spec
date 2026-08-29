# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: Zheng Junjie <zhengjunjie@iscas.ac.cn>
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
# SPDX-FileContributor: Zitao Zhou <zitao.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global srcname wheel
# Virtual provides for the packages bundled by wheel.
# %%{_rpmconfigdir}/pythonbundles.py src/wheel/vendored/vendor.txt --namespace 'python%%{python3_pkgversion}dist'
%global bundled %{expand:
Provides: bundled(python%{python3_pkgversion}dist(packaging)) = 24
}

Name:           python-wheel
Version:        0.48.0
Release:        %autorelease
Summary:        Built-package format for Python
License:        MIT AND (Apache-2.0 OR BSD-2-Clause)
URL:            https://github.com/pypa/wheel
#!RemoteAsset:  sha256:c3beae7abe07db04c2303502e4483122cc6b3686a7dfb0d8ca050dd034d5bdfe
Source:         %{url}/archive/%{version}/wheel-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    pyproject

BuildOption(install):  -l wheel
# Although we have setuptools, maybe include in test is a bad idea
BuildOption(check):  -e wheel.bdist_wheel

BuildRequires:  pyproject-rpm-macros
BuildRequires:  pkgconfig(python3)

Provides:       python3-%{srcname} = %{version}-%{release}
%python_provide python3-%{srcname}

%{bundled}

%description
This is a command line tool for manipulating Python wheel files,
as defined in PEP 427. It contains the following functionality:

- Convert .egg archives into .whl.
- Unpack wheel archives.
- Repack wheel archives.
- Add or remove tags in existing wheel archives.

%generate_buildrequires
%pyproject_buildrequires

%install -a
mv %{buildroot}%{_bindir}/wheel{,-3}
ln -s wheel-3 %{buildroot}%{_bindir}/wheel

%files -f %{pyproject_files}
%doc README.rst
%{_bindir}/wheel-3
%{_bindir}/wheel

%changelog
%autochangelog
