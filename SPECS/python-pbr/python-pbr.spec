# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Li Guan <guanli.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global srcname pbr

Name:           python-%{srcname}
Version:        7.1.3
Release:        %autorelease
Summary:        Python Build Reasonableness
License:        Apache-2.0
URL:            https://opendev.org/openstack/pbr
#!RemoteAsset:  sha256:9a4a85b84e906337708009af0b5f5cdabeeb72d4dc213c9e97974da54fd9acc5
Source0:        https://files.pythonhosted.org/packages/source/p/%{srcname}/%{srcname}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    pyproject

BuildOption(install):  -l %{srcname}
# The bundled test modules require the separate OpenStack test harness.
BuildOption(check):  -e 'pbr.tests*'
# The optional documentation extension requires Sphinx.
BuildOption(check):  -e 'pbr.sphinxext'

BuildRequires:  pyproject-rpm-macros
BuildRequires:  pkgconfig(python3)

Provides:       python3-%{srcname} = %{version}-%{release}
%python_provide python3-%{srcname}

%description
PBR extends setuptools to derive package metadata, versions and file lists
from declarative configuration and Git history.

%generate_buildrequires
%pyproject_buildrequires

%check -a
# Verify the installed command can read the wheel's release metadata.
PYTHONPATH=%{buildroot}%{python3_sitelib} %{buildroot}%{_bindir}/pbr info --short pbr | grep -Fx '%{version}'

%files -f %{pyproject_files}
%doc README.rst
%{_bindir}/pbr

%changelog
%autochangelog
