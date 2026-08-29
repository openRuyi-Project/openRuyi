# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: purofle <yuguo.or@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           perl-Log-Any
Version:        1.720
Release:        %autorelease
Summary:        Bringing loggers and listeners together
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/dist/Log-Any
#!RemoteAsset:  sha256:1fa8a6121dce297406f67adbcb4d92db01e9dd85781cb6ef710dc333bb9cfd56
Source0:        https://cpan.metacpan.org/authors/id/P/PR/PREACTION/Log-Any-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    perlmaker

Patch2000:      2000-isolate-syslog-test-env.patch

BuildOption(build):  INSTALLDIRS=vendor

BuildRequires:  make
BuildRequires:  perl-rpm-packaging
BuildRequires:  perl-rpm-macros
BuildRequires:  perl-macros
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(Devel::StackTrace)
BuildRequires:  perl(IO::Handle)
BuildRequires:  perl(IPC::Open3)
BuildRequires:  perl(Test::More)

%description
Log::Any provides a standard log production API for modules.
Log::Any::Adapter allows applications to choose the mechanism for log
consumption, whether screen, file or another logging mechanism like
Log::Dispatch or Log::Log4perl.

%files -f %{name}.files
%doc CONTRIBUTING.md Changes README
%license LICENSE

%changelog
%autochangelog
