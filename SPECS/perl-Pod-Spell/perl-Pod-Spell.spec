# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: Zheng Junjie <zhengjunjie@iscas.ac.cn>
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           perl-Pod-Spell
Version:        1.27
Release:        %autorelease
Summary:        Formatter for spellchecking Pod
License:        Artistic-2.0
URL:            https://metacpan.org/dist/Pod-Spell
#!RemoteAsset
Source0:        http://www.cpan.org/authors/id/H/HA/HAARG/Pod-Spell-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  make
BuildRequires:  perl-rpm-packaging
BuildRequires:  perl-macros
BuildRequires:  perl >= 5.8.1
BuildRequires:  perl(Carp)
BuildRequires:  perl(Class::Tiny)
BuildRequires:  perl(constant)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(File::ShareDir)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(File::Temp)
BuildRequires:  perl(IO::Handle)
BuildRequires:  perl(IPC::Open3)
BuildRequires:  perl(Lingua::EN::Inflect)
BuildRequires:  perl(locale)
BuildRequires:  perl(parent)
BuildRequires:  perl(Pod::Escapes)
BuildRequires:  perl(Pod::Simple) >= 3.27
BuildRequires:  perl(POSIX)
BuildRequires:  perl(Test::More) >= 0.88
BuildRequires:  perl(Text::Wrap)
# Manual
BuildRequires:  perl(File::ShareDir::Install)

Requires:       perl(Pod::Simple) >= 3.27

%description
Pod::Spell is a Pod formatter whose output is good for spellchecking.
Pod::Spell is rather like Pod::Text, except that it doesn't put much effort
into actual formatting, and it suppresses things that look like Perl
symbols or Perl jargon (so that your spellchecking program won't complain
about mystery words like "$thing" or "Foo::Bar" or "hashref").

%prep
%setup -q -n Pod-Spell-%{version}

%build
perl Makefile.PL INSTALLDIRS=vendor
%{make_build}

%install
%perl_make_install
%perl_process_packlist
%perl_gen_filelist

%files -f %{name}.files
%doc Changes CONTRIBUTING prereqs.yml README weaver.ini

%changelog
%autochangelog
