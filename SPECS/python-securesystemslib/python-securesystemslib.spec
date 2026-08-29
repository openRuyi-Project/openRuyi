# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Kimmy <yucheng.or@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global srcname securesystemslib

Name:           python-%{srcname}
Version:        1.4.0
Release:        %autorelease
Summary:        Cryptographic and general-purpose routines for secure systems
License:        MIT
URL:            https://github.com/secure-systems-lab/securesystemslib
VCS:            git:https://github.com/secure-systems-lab/securesystemslib.git
#!RemoteAsset:  sha256:faea87be0f9c4b4277a5fa1b54bf9bfd807be9a94ab11be6c557dc8b75c43285
Source0:        https://files.pythonhosted.org/packages/source/s/%{srcname}/%{srcname}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    pyproject

BuildOption(install):  -l %{srcname}
BuildOption(check):  %{srcname}

BuildRequires:  pyproject-rpm-macros
BuildRequires:  pkgconfig(python3)
# Upstream pyproject.toml pins build-system.requires to hatchling==1.29.0.
BuildRequires:  python3dist(hatchling) = 1.29

Provides:       python3-%{srcname} = %{version}-%{release}
%python_provide python3-%{srcname}

%description
securesystemslib provides cryptographic key, signature, and canonical JSON
helpers shared by The Update Framework and other secure software systems.

%generate_buildrequires
%pyproject_buildrequires

%files -f %{pyproject_files}
%doc CHANGELOG.md README.md
%license LICENSE

%changelog
%autochangelog
