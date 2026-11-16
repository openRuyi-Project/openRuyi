# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: A.Donz <avrova.minix@donz.si>
# SPDX-FileContributor: MMLA-org <https://github.com/MMLA-org>
#
# SPDX-License-Identifier: MulanPSL-2.0

# Sponsored by cha86.dev <https://cha86.dev>

%global srcname genson

Name:           python-%{srcname}
Version:        1.4.0
Release:        %autorelease
Summary:        JSON Schema generator for Python
License:        MIT
URL:            https://github.com/wolverdude/GenSON
#!RemoteAsset:  sha256:bc7f1c1bae87a21ca44d81149aec95a3f4468d676de9b8b08caa064f3c50b3da
Source0:        https://files.pythonhosted.org/packages/source/g/%{srcname}/%{srcname}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    pyproject
BuildOption(install):  -l %{srcname}
BuildOption(install):  +auto

BuildRequires:  pyproject-rpm-macros
BuildRequires:  pkgconfig(python3)
BuildRequires:  python3dist(pip)
BuildRequires:  python3dist(pytest)
BuildRequires:  python3dist(setuptools)

Provides:       python3-%{srcname} = %{version}-%{release}
%python_provide python3-%{srcname}

%description
GenSON generates and merges JSON Schemas from Python objects and JSON data.

%generate_buildrequires
%pyproject_buildrequires

%check -a
%pytest -q

%files -f %{pyproject_files}
%doc README.rst
%license LICENSE

%changelog
%autochangelog
