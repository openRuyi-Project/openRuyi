# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: yihong <yihong.or@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           perl-IPC-Run
Version:        20260402.0
Release:        %autorelease
Summary:        System and background process runner with piping
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/dist/IPC-Run
#!RemoteAsset:  sha256:d6a326a8b1ffb19495dea4ff5a09ef138bf3562ab1b069d3fb7efbc77b9f6aca
Source0:        https://cpan.metacpan.org/authors/id/T/TO/TODDR/IPC-Run-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    perlmaker

BuildOption(build):  INSTALLDIRS=vendor

BuildRequires:  make
BuildRequires:  perl-rpm-packaging
BuildRequires:  perl-rpm-macros
BuildRequires:  perl-macros
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(IO::Pty) >= 1.25
BuildRequires:  perl(Readonly::Array)
BuildRequires:  perl(Test::More)

Requires:       perl(IO::Pty) >= 1.25

%description
IPC::Run starts child processes with flexible piping, redirection and pseudo
terminal support.

%files -f %{name}.files
%doc AI_POLICY.md Changelog README.md eg
%license LICENSE

%changelog
%autochangelog
