# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Jvle <keke.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global srcname cart

Name:           python-%{srcname}
Version:        1.2.3
Release:        %autorelease
Summary:        Python implementation of the CaRT library for (un)inerting files.
License:        MIT
URL:            https://github.com/CybercentreCanada/cart
# no source distribution files available for this release, so we have to use the GitHub archive instead.
#!RemoteAsset:  sha256:4b2921931b95c4a5ba81d690f8dc3107a0a1fab04470c146251faf6d6ed1a151
Source0:        https://github.com/CybercentreCanada/cart/archive/v%{version}/cart-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    pyproject

Patch0:         0001-python-cart-1.2.2-cryptodomex.patch

BuildOption(install):  -l %{srcname}

BuildRequires:  pyproject-rpm-macros
BuildRequires:  pkgconfig(python3)

Provides:       python3-%{srcname} = %{version}-%{release}
%python_provide python3-%{srcname}

%description
This package provides Python support for CaRT (Compressed and RC4
Transport). The CaRT file format is used to store/transfer malware
and its associated metadata. It neuters the malware so it cannot be
executed and encrypts it so anti-virus software cannot flag the CaRT
file as malware.

%prep -a
sed -i '/#!\/usr\/bin\/env python/d' cart/cart.py

%generate_buildrequires
%pyproject_buildrequires

%check -a
%{py3_test_envvars} %{python3} -m unittest

%files -f %{pyproject_files}
%{_bindir}/cart
%license LICENSE.md
%doc README.md

%changelog
%autochangelog
