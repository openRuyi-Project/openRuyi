# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global srcname pyyaml-ft
%global pypi_name pyyaml_ft

Name:           python-%{srcname}
Version:        8.0.0
Release:        %autorelease
Summary:        YAML parser and emitter for Python with free-threading support
License:        MIT
URL:            https://github.com/Quansight-Labs/pyyaml-ft
#!RemoteAsset:  sha256:0c947dce03954c7b5d38869ed4878b2e6ff1d44b08a0d84dc83fdad205ae39ab
Source0:        https://files.pythonhosted.org/packages/source/p/%{srcname}/%{pypi_name}-%{version}.tar.gz
BuildSystem:    pyproject

BuildOption(build):  -C--global-option=--with-libyaml
BuildOption(install):  -l yaml_ft _yaml_ft
BuildOption(check):  yaml_ft

BuildRequires:  pyproject-rpm-macros
BuildRequires:  pkgconfig(yaml-0.1)
BuildRequires:  pkgconfig(python3)
BuildRequires:  python3dist(cython) >= 3.1
BuildRequires:  python3dist(pip)
BuildRequires:  python3dist(setuptools)
BuildRequires:  python3dist(wheel)

Provides:       python3-%{srcname}
Provides:       python3-%{srcname} = %{version}-%{release}
Provides:       python3-%{srcname}%{?_isa} = %{version}-%{release}
%python_provide python3-%{srcname}

%description
PyYAML-ft provides a YAML parser and emitter for Python with support for
free-threaded Python 3.13 runtimes.

%generate_buildrequires
%pyproject_buildrequires

%files -f %{pyproject_files}
%doc README.md CHANGES
%license LICENSE

%changelog
%autochangelog
