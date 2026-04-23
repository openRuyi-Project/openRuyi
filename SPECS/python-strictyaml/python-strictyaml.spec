# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Li Guan <guanli.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global srcname strictyaml

Name:           python-%{srcname}
Version:        1.7.3
Release:        %autorelease
Summary:        Type-safe YAML parser and validator
License:        MIT
URL:            https://hitchdev.com/strictyaml/
VCS:            git:https://github.com/crdoconnor/strictyaml.git
#!RemoteAsset:  sha256:22f854a5fcab42b5ddba8030a0e4be51ca89af0267961c8d6cfa86395586c407
Source0:        https://files.pythonhosted.org/packages/source/s/%{srcname}/%{srcname}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    pyproject

BuildOption(install):  -l %{srcname}

BuildRequires:  pyproject-rpm-macros
BuildRequires:  pkgconfig(python3)
BuildRequires:  python3dist(ruamel-yaml-clib)

Requires:       python3dist(ruamel-yaml-clib)

Provides:       python3-%{srcname} = %{version}-%{release}
%python_provide python3-%{srcname}

%description
StrictYAML is a type-safe YAML parser that parses and
validates a restricted subset of the YAML specification.

%generate_buildrequires
%pyproject_buildrequires

%files -f %{pyproject_files}
%doc README.md
%license LICENSE.txt

%changelog
%autochangelog
