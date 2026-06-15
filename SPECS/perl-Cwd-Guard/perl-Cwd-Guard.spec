# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: yihong <yihong.or@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           perl-Cwd-Guard
Version:        0.05
Release:        %autorelease
Summary:        Temporary changing working directory
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/dist/Cwd-Guard
#!RemoteAsset:  sha256:7afc7ca2b9502e440241938ad97a3e7ebd550180ebd6142e1db394186b268e77
Source0:        https://cpan.metacpan.org/authors/id/K/KA/KAZEBURO/Cwd-Guard-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    perlbuild

BuildOption(build):  --installdirs=vendor
BuildOption(install):  --destdir=%{buildroot} --create_packlist=0

BuildRequires:  perl-rpm-packaging
BuildRequires:  perl-rpm-macros
BuildRequires:  perl-macros
BuildRequires:  perl(Module::Build) >= 0.38
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Test::Requires)

%description
Cwd::Guard changes the current working directory for a limited scope and
restores the previous directory when the guard object is destroyed.

%files -f %{name}.files
%doc Changes README.md
%license LICENSE

%changelog
%autochangelog
