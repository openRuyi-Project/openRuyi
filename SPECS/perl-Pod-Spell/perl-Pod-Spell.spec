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
#!RemoteAsset:  sha256:7ef56c9229f3efbc71a0462ce44490c0dd49fbf3b21fe85bb08b1eeac6f7b063
Source0:        https://www.cpan.org/authors/id/H/HA/HAARG/Pod-Spell-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    perlmaker

BuildOption(build):  INSTALLDIRS=vendor

BuildRequires:  make
BuildRequires:  perl-rpm-packaging
BuildRequires:  perl-rpm-macros
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
BuildRequires:  perl(File::ShareDir::Install)
BuildRequires:  perl(Test::More) >= 0.88
BuildRequires:  perl(Text::Wrap)

Requires:       perl(Pod::Simple) >= 3.27

%description
Pod::Spell is a Pod formatter whose output is good for spellchecking.
Pod::Spell is rather like Pod::Text, except that it doesn't put much effort
into actual formatting, and it suppresses things that look like Perl
symbols or Perl jargon (so that your spellchecking program won't complain
about mystery words like "$thing" or "Foo::Bar" or "hashref").

%files -f %{name}.files
%doc Changes CONTRIBUTING prereqs.yml README weaver.ini

%changelog
%autochangelog
