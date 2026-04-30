# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: HNO3Miracle <xiangao.or@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global srcname beautifulsoup4

Name:           python-beautifulsoup4
Version:        4.14.3
Release:        %autorelease
Summary:        HTML/XML parser for quick-turnaround applications like screen-scraping
License:        MIT
URL:            http://www.crummy.com/software/BeautifulSoup/
#!RemoteAsset:  sha256:6292b1c5186d356bba669ef9f7f051757099565ad9ada5dd630bd9de5fa7fb86
Source0:        https://files.pythonhosted.org/packages/source/b/%{srcname}/%{srcname}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    pyproject

BuildOption(install):  -l bs4

# Patches from upstream
# https://git.launchpad.net/beautifulsoup/commit/?id=ec4a722af07341c4aa3fe604b077a1f773c6fdd2
# Skip the lxml surrogate-character test with older libxml2 releases
Patch0:         0001-Skip-the-lxml-tree-builder-s-test_surrogate_in_chara.patch
# https://git.launchpad.net/beautifulsoup/commit/?id=55f655ffb7ef03bdd1df0f013743831fe54e3c7a
# Fix html.parser numeric character reference handling for newer Python
Patch1:         0002-Change-the-html.parser-tree-builder-s-code-for-handl.patch
# Local openRuyi patch to adjust the surrogate-character test expectation for Python 3.15
Patch2000:         2000-python-beautifulsoup4-4.14.3-test.patch

BuildRequires:  pyproject-rpm-macros
BuildRequires:  pkgconfig(python3)
BuildRequires:  python3dist(pip)
BuildRequires:  python3dist(setuptools)
BuildRequires:  python3dist(hatchling)
BuildRequires:  python3dist(typing-extensions)
BuildRequires:  python3dist(packaging)
BuildRequires:  python3dist(soupsieve)
BuildRequires:  python3dist(pytest)
BuildRequires:  python3dist(html5lib)
BuildRequires:  python3dist(lxml)

Provides:       python3-beautifulsoup4 = %{version}-%{release}
%python_provide python3-beautifulsoup4

%description
Beautiful Soup is a Python HTML/XML parser designed for quick
turnaround projects like screen-scraping.

%generate_buildrequires
%pyproject_buildrequires

%prep
%autosetup -N -n %{srcname}-%{version}
# Apply upstream patches and the local Python 3.15 test adjustment
%autopatch -p1 -M 2

# Physically remove tox to be sure
rm -f tox.ini

%check -a
%pytest

%files -f %{pyproject_files}
%license LICENSE
%doc NEWS.txt CHANGELOG

%changelog
%autochangelog
