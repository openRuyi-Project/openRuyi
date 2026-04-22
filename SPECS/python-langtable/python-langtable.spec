# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global srcname langtable

Name:           python-%{srcname}
Version:        0.0.70
Release:        %autorelease
Summary:        guess reasonable defaults for locale, keyboard, territory, ...
License:        GPL-3.0-or-later
URL:            https://github.com/mike-fabian/langtable
#!RemoteAsset:  sha256:725b94121856a3b76d2345e8596954b82ed1eda78513e55ac55fbe4a4823e66e
Source0:        https://files.pythonhosted.org/packages/source/l/%{srcname}/%{srcname}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    pyproject

BuildOption(install):  %{srcname}

BuildRequires:  pyproject-rpm-macros
BuildRequires:  pkgconfig(python3)
BuildRequires:  perl

Provides:       python3-%{srcname} = %{version}-%{release}
%python_provide python3-%{srcname}

%description
langtable is used to guess reasonable defaults for locale, keyboard layout,
territory, and language, if part of that information is already known. For
example, guess the territory and the keyboard layout if the language
is known or guess the language and keyboard layout if the territory is
already known.

%generate_buildrequires
%pyproject_buildrequires

%build -p
%__perl -pi -e "s,_DATADIR = '(.*)',_DATADIR = '%{_datadir}/langtable'," langtable/langtable.py

%files -f %{pyproject_files}
%doc README* ChangeLog test_cases.py langtable/schemas/*.rng
%license COPYING unicode-license.txt

%changelog
%autochangelog
