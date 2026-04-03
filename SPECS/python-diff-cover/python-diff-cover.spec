# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Jvle <keke.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global srcname diff-cover
%global pypi_name diff_cover

Name:           python-%{srcname}
Version:        10.2.0
Release:        %autorelease
Summary:        Automatically find diff lines that need test coverage
License:        Apache-2.0
URL:            https://github.com/Bachmann1234/diff-cover
#!RemoteAsset:  sha256:61bf83025f10510c76ef6a5820680cf61b9b974e8f81de70c57ac926fa63872a
Source0:        https://files.pythonhosted.org/packages/source/d/%{pypi_name}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    pyproject

BuildOption(install):  %{pypi_name}

BuildRequires:  help2man
BuildRequires:  pkgconfig(python3)
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3dist(pytest)
BuildRequires:  python3dist(pytest-mock)
BuildRequires:  python3dist(pytest-datadir)

Provides:       python3-%{srcname} = %{version}-%{release}
%python_provide python3-%{srcname}

%description
Diff coverage is the percentage of new or modified lines that are covered by
tests. This provides a clear and achievable standard for code review: If you
touch a line of code, that line should be covered. Code coverage is *every*
developer's responsibility!

The diff-cover command line tool compares an XML coverage report with the
output of git diff. It then reports coverage information for lines in the
diff.

%generate_buildrequires
%pyproject_buildrequires

%install -a
mkdir -p %{buildroot}%{_mandir}/man1
PYTHONPATH=%{buildroot}%{python3_sitelib} \
    help2man --no-info --version-string 'diff-cover %{version}' \
        -o %{buildroot}%{_mandir}/man1/diff-cover.1 \
        %{buildroot}%{_bindir}/diff-cover

PYTHONPATH=%{buildroot}%{python3_sitelib} \
    help2man --no-info --version-string 'diff-quality %{version}' \
        -o %{buildroot}%{_mandir}/man1/diff-quality.1 \
        %{buildroot}%{_bindir}/diff-quality

%check -a
%pytest -k "not TestDiffQualityIntegration and not TestFlake8QualityReporterTest"

%files -f %{pyproject_files}
%license LICENSE
%doc README.rst
%{_mandir}/man1/diff-cover.1*
%{_mandir}/man1/diff-quality.1*
%{_bindir}/diff-cover
%{_bindir}/diff-quality

%changelog
%{?autochangelog}
