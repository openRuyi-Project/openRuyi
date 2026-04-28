# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global srcname django

Name:           python-%{srcname}
Version:        5.2.4
Release:        %autorelease
Summary:        A high-level Python Web framework
License:        BSD-3-Clause AND PSF-2.0 AND MIT AND OFL-1.1
URL:            https://www.djangoproject.com/
#!RemoteAsset
Source0:        https://files.pythonhosted.org/packages/source/d/%{srcname}/%{srcname}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    pyproject

BuildOption(install):  -l %{srcname}

BuildRequires:  pyproject-rpm-macros
BuildRequires:  pkgconfig(python3)
BuildRequires:  python3dist(asgiref)
# Tests?
BuildRequires:  python3dist(jinja2)

Provides:       python3-%{srcname}
%python_provide python3-%{srcname}

%description
Django is a high-level Python Web framework that encourages rapid
development and a clean, pragmatic design. It focuses on automating as
much as possible and adhering to the DRY (Don't Repeat Yourself)
principle.

%package        bash-completion
Summary:        Bash completion files for Django
BuildRequires:  bash-completion
Requires:       bash-completion

%description    bash-completion
This package contains the Bash completion files form Django high-level
Python Web framework.

%generate_buildrequires
%pyproject_buildrequires

%install -a
# install man pages (for the main executable only)
mkdir -p %{buildroot}%{_mandir}/man1/
cp -p docs/man/* %{buildroot}%{_mandir}/man1/

# install bash completion script
mkdir -p %{buildroot}%{bash_completions_dir}
install -m 0644 -p extras/django_bash_completion \
 %{buildroot}%{bash_completions_dir}/django-admin

for file in manage.py ; do
  ln -s django-admin.py %{buildroot}%{bash_completions_dir}/$file
done

# remove .po files
find %{buildroot} -name "*.po" | xargs rm -f
sed -i '/.po$/d' %{pyproject_files}

%check
# many contrib modules assume a configured app, "Requested setting INSTALLED_APPS..."
# the rest needs optional dependencies
%{pyproject_check_import \
   -e 'django.contrib.*' \
   -e 'django.core.serializers.pyyaml' \
   -e 'django.db.backends.mysql*' \
   -e 'django.db.backends.oracle*' \
   -e 'django.db.backends.postgresql*'}

%files -f %{pyproject_files}
%doc AUTHORS README.rst
%{_bindir}/django-admin
%{_mandir}/man1/django-admin.1*

%files bash-completion
%{bash_completions_dir}/*

%changelog
%{?autochangelog}
