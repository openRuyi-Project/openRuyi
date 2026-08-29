# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Kimmy <yucheng.or@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global srcname sigstore-rekor-types
%global pypi_name sigstore_rekor_types

Name:           python-%{srcname}
Version:        0.0.18
Release:        %autorelease
Summary:        Python models for Rekor API types
License:        Apache-2.0
URL:            https://github.com/trailofbits/sigstore-rekor-types
VCS:            git:https://github.com/trailofbits/sigstore-rekor-types.git
#!RemoteAsset:  sha256:19aef25433218ebf9975a1e8b523cc84aaf3cd395ad39a30523b083ea7917ec5
Source0:        https://files.pythonhosted.org/packages/source/s/%{srcname}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    pyproject

BuildOption(install):  -l rekor_types
BuildOption(check):  rekor_types

BuildRequires:  pyproject-rpm-macros
BuildRequires:  pkgconfig(python3)
BuildRequires:  python3dist(email-validator) >= 2
BuildRequires:  python3dist(pydantic) >= 2
BuildRequires:  python3dist(pydantic) < 3
BuildRequires:  python3dist(setuptools) >= 75

Provides:       python3-%{srcname} = %{version}-%{release}
%python_provide python3-%{srcname}

%description
Python models generated from the API types used by Sigstore's Rekor
transparency log.

%prep -a
# Expand the pydantic email extra because it has no RPM virtual provide.
sed -i 's/pydantic\[email\]/pydantic/' pyproject.toml

%generate_buildrequires
%pyproject_buildrequires

%files -f %{pyproject_files}
%doc README.md
%license LICENSE

%changelog
%autochangelog
