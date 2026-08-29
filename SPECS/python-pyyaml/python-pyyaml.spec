# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: Zheng Junjie <zhengjunjie@iscas.ac.cn>
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global srcname PyYAML
%global pypi_name pyyaml

Name:           python-pyyaml
Version:        6.0.3
Release:        %autorelease
Summary:        YAML parser and emitter for Python
License:        MIT
URL:            https://github.com/yaml/pyyaml
#!RemoteAsset:  sha256:d76623373421df22fb4cf8817020cbb7ef15c725b9d5e45f17e189bfc384190f
Source0:        https://files.pythonhosted.org/packages/source/p/%{pypi_name}/%{pypi_name}-%{version}.tar.gz
BuildSystem:    pyproject

BuildOption(install):  yaml _yaml

BuildRequires:  pyproject-rpm-macros
BuildRequires:  pkgconfig(yaml-0.1)
BuildRequires:  pkgconfig(python3)
BuildRequires:  python3dist(pytest)

Provides:       python3-pyyaml = %{version}-%{release}
Provides:       python3-pyyaml%{?_isa} = %{version}-%{release}
%python_provide python3-pyyaml

%description
YAML is a data serialization format designed for human readability and
interaction with scripting languages.  PyYAML is a YAML parser and
emitter for Python.

PyYAML features a complete YAML 1.1 parser, Unicode support, pickle
support, capable extension API, and sensible error messages.  PyYAML
supports standard YAML tags and provides Python-specific tags that
allow to represent an arbitrary Python object.

PyYAML is applicable for a broad range of tasks from complex
configuration files to object serialization and persistence.

%prep -a
chmod a-x examples/yaml-highlight/yaml_hl.py

%generate_buildrequires
%pyproject_buildrequires

%files -f %{pyproject_files}
%doc CHANGES README.md examples

%changelog
%autochangelog
