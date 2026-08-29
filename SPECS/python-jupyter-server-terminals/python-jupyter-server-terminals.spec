# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: zhangjinqiang <jinqiang.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global srcname jupyter-server-terminals
%global pypi_name jupyter_server_terminals

Name:           python-%{srcname}
Version:        0.5.4
Release:        %autorelease
Summary:        Terminal support for Jupyter Server
License:        BSD-3-Clause
URL:            https://github.com/jupyter-server/jupyter_server_terminals
#!RemoteAsset:  sha256:bbda128ed41d0be9020349f9f1f2a4ab9952a73ed5f5ac9f1419794761fb87f5
Source0:        https://files.pythonhosted.org/packages/source/j/%{pypi_name}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    pyproject

BuildOption(install):  -l jupyter_server_terminals

BuildRequires:  pkgconfig(python3)
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3dist(hatchling)
BuildRequires:  python3dist(pip)
BuildRequires:  python3dist(terminado)

Provides:       python3-%{srcname} = %{version}-%{release}
%python_provide python3-%{srcname}

%description
Jupyter Server Terminals provides a Jupyter Server extension for terminal
sessions.

%generate_buildrequires
%pyproject_buildrequires

%install -a
mv %{buildroot}%{_prefix}%{_sysconfdir} %{buildroot}%{_sysconfdir}

# Skip tests: No module named 'jupyter_server' (circular dependency)
%check

%files -f %{pyproject_files}
%doc README.md
%license LICENSE
%{_sysconfdir}/jupyter/jupyter_server_config.d/jupyter_server_terminals.json

%changelog
%autochangelog
