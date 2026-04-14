# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: purofle <yuguo.or@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           perl-Log-Any
Version:        1.719
Release:        %autorelease
Summary:        Bringing loggers and listeners together
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/dist/Log-Any
#!RemoteAsset:  sha256:69774be9e6f1d91c3e112f834f09bc8ce6f5d336f456aa1de3985b8de05e07b6
Source0:        https://cpan.metacpan.org/authors/id/P/PR/PREACTION/Log-Any-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  make
BuildRequires:  perl-rpm-packaging
BuildRequires:  perl-macros
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(IO::Handle)
BuildRequires:  perl(IPC::Open3)
BuildRequires:  perl(Test::More)

%description
Log::Any provides a standard log production API for modules.
Log::Any::Adapter allows applications to choose the mechanism for log
consumption, whether screen, file or another logging mechanism like
Log::Dispatch or Log::Log4perl.

%prep
%setup -q -n Log-Any-%{version}

%build
perl Makefile.PL INSTALLDIRS=vendor
%{make_build}

%install
%perl_make_install
%perl_process_packlist
%perl_gen_filelist

%files -f %{name}.files
%doc CONTRIBUTING.md Changes README
%license LICENSE

%changelog
%autochangelog
