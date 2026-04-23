# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global srcname ruamel.yaml

Name:           python-ruamel-yaml
Version:        0.18.16
Release:        %autorelease
Summary:        YAML 1.2 loader/dumper package for Python
License:        MIT
URL:            https://sourceforge.net/projects/ruamel-yaml/
#!RemoteAsset:  sha256:a6e587512f3c998b2225d68aa1f35111c29fad14aed561a26e73fab729ec5e5a
Source0:        https://files.pythonhosted.org/packages/source/r/%{srcname}/%{srcname}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    pyproject

BuildOption(install):  -l ruamel

BuildRequires:  pyproject-rpm-macros
BuildRequires:  pkgconfig(python3)

Provides:       python3-ruamel-yaml = %{version}-%{release}
%python_provide python3-ruamel-yaml

%description
ruamel.yaml is a YAML parser/emitter that supports roundtrip preservation of
comments, seq/map flow style, and map key order.

%generate_buildrequires
%pyproject_buildrequires

%files -f %{pyproject_files}
%doc README.md

%changelog
%autochangelog
