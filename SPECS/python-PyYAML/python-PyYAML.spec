# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: Zheng Junjie <zhengjunjie@iscas.ac.cn>
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global srcname PyYAML
%global pypi_name pyyaml

Name:           python-%{srcname}
Version:        6.0.2
Release:        %autorelease
Summary:        YAML parser and emitter for Python
License:        MIT
URL:            https://github.com/yaml/pyyaml
#!RemoteAsset:  sha256:d584d9ec91ad65861cc08d42e834324ef890a082e591037abe114850ff7bbc3e
Source0:        https://files.pythonhosted.org/packages/source/p/%{pypi_name}/%{pypi_name}-%{version}.tar.gz
BuildSystem:    pyproject

BuildOption(install):  yaml _yaml

BuildRequires:  pyproject-rpm-macros
BuildRequires:  pkgconfig(yaml-0.1)
BuildRequires:  pkgconfig(python3)
BuildRequires:  python3dist(pytest)

Provides:       python3-%{srcname} = %{version}-%{release}
Provides:       python3-%{srcname}%{?_isa} = %{version}-%{release}
%python_provide python3-%{srcname}

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

# remove pre-generated file
rm -rf ext/_yaml.c

%generate_buildrequires
%pyproject_buildrequires

%files -f %{pyproject_files}
%doc CHANGES README.md examples

%changelog
%autochangelog
