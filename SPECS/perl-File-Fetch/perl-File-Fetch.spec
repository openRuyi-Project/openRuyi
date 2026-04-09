# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           perl-File-Fetch
Version:        1.08
Release:        %autorelease
Summary:        Generic file fetching mechanism
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/dist/File-Fetch
#!RemoteAsset
Source0:        http://www.cpan.org/authors/id/B/BI/BINGOS/File-Fetch-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  make
BuildRequires:  perl-rpm-packaging
BuildRequires:  perl-macros
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(File::Basename)
BuildRequires:  perl(File::Copy)
BuildRequires:  perl(File::Path)
BuildRequires:  perl(File::Spec) >= 0.82
BuildRequires:  perl(IPC::Cmd) >= 0.42
BuildRequires:  perl(Locale::Maketext::Simple)
BuildRequires:  perl(Module::Load::Conditional) >= 0.66
BuildRequires:  perl(Params::Check) >= 0.07
BuildRequires:  perl(Test::More)

Requires:       perl(File::Spec) >= 0.82
Requires:       perl(IPC::Cmd) >= 0.42
Requires:       perl(Module::Load::Conditional) >= 0.66
Requires:       perl(Params::Check) >= 0.07

%description
File::Fetch is a generic file fetching mechanism.

%prep
%setup -q -n File-Fetch-%{version}

%build
perl Makefile.PL INSTALLDIRS=vendor
%{make_build}

%install
%perl_make_install
%perl_process_packlist
%perl_gen_filelist

%files -f %{name}.files
%doc CHANGES README

%changelog
%autochangelog
