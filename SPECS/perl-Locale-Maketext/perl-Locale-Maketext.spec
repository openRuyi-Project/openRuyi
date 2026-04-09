# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           perl-Locale-Maketext
Version:        1.33
Release:        %autorelease
Summary:        Framework for localization
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/dist/Locale-Maketext
#!RemoteAsset
Source0:        http://www.cpan.org/authors/id/T/TO/TODDR/Locale-Maketext-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  make
BuildRequires:  perl-rpm-packaging
BuildRequires:  perl-macros
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(I18N::LangTags) >= 0.31
BuildRequires:  perl(I18N::LangTags::Detect)
BuildRequires:  perl(parent)
BuildRequires:  perl(Test::More)

Requires:       perl(I18N::LangTags) >= 0.31

%description
It is a common feature of applications (whether run directly, or via the
Web) for them to be "localized" -- i.e., for them to a present an English
interface to an English-speaker, a German interface to a German-speaker,
and so on for all languages it's programmed with. Locale::Maketext is a
framework for software localization; it provides you with the tools for
organizing and accessing the bits of text and text-processing code that you
need for producing localized applications.

%prep
%setup -q -n Locale-Maketext-%{version}

%build
perl Makefile.PL INSTALLDIRS=vendor
%{make_build}

%install
%perl_make_install
%perl_process_packlist
%perl_gen_filelist

%files -f %{name}.files
%doc ChangeLog perlcriticrc README

%changelog
%autochangelog
