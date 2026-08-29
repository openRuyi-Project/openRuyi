# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: purofle <yuguo.or@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global srcname pycotap

Name:           python-%{srcname}
Version:        1.3.1
Release:        %autorelease
Summary:        A tiny test runner that outputs TAP results to standard output
License:        MIT
URL:            https://github.com/remko/pycotap
#!RemoteAsset:  sha256:674355f01300be03df7f871784e498652c2d89ac19cd77ee8e61652634a2f83a
Source0:        https://files.pythonhosted.org/packages/source/p/%{srcname}/%{srcname}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    pyproject

BuildOption(install):  -l %{srcname}

BuildRequires:  pyproject-rpm-macros
BuildRequires:  pkgconfig(python3)
BuildRequires:  python3dist(pip)
BuildRequires:  python3dist(pytest)
BuildRequires:  python3dist(setuptools)
BuildRequires:  python3dist(wheel)

Provides:       python3-%{srcname} = %{version}-%{release}
%python_provide python3-%{srcname}

%description
pycotap is a simple Python test runner for unittest that outputs Test
Anything Protocol results directly to standard output.

%generate_buildrequires
%pyproject_buildrequires

%install -a
find %{buildroot}/%{python3_sitelib} -name '*.py' | xargs sed -i '/^#!/d'
%__rm -f %{buildroot}/usr/COPYING

%files -f %{pyproject_files}
%doc README.md
%license COPYING

%changelog
%autochangelog
