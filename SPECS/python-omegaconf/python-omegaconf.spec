# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Li Guan <guanli.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global srcname omegaconf

Name:           python-%{srcname}
Version:        2.3.0
Release:        %autorelease
Summary:        Flexible Python configuration system
License:        BSD-3-Clause
URL:            https://github.com/omry/omegaconf
#!RemoteAsset:  sha256:d5d4b6d29955cc50ad50c46dc269bcd92c6e00f5f90d23ab5fee7bfca4ba4cc7
Source0:        https://files.pythonhosted.org/packages/source/o/%{srcname}/%{srcname}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    pyproject

BuildOption(install):  -l %{srcname}

BuildRequires:  pyproject-rpm-macros
BuildRequires:  pkgconfig(python3)
BuildRequires:  java-latest-openjdk

Provides:       python3-%{srcname} = %{version}-%{release}
%python_provide python3-%{srcname}

%description
OmegaConf is a hierarchical configuration system,
with support for merging configurations from multiple
sources (YAML config files, dataclasses/objects and CLI arguments)
providing a consistent API regardless of how the configuration was created.

%generate_buildrequires
%pyproject_buildrequires

%install -a
# Drop unnecessary pydevd_plugins to avoid packaging unwanted debug tools.
rm -rf %{buildroot}%{python3_sitelib}/pydevd_plugins/

%files -f %{pyproject_files}
%doc README.md
%license LICENSE

%changelog
%autochangelog
