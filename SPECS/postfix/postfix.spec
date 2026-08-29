# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Li Guan <guanli.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global postfix_user postfix
%global postdrop_group postdrop
%global postfix_config_dir %{_sysconfdir}/postfix
%global postfix_daemon_dir %{_libexecdir}/postfix
%global postfix_queue_dir %{_var}/spool/postfix
%global postfix_data_dir %{_var}/lib/postfix

Name:           postfix
Version:        3.11.5
Release:        %autorelease
Summary:        Postfix Mail Transport Agent
License:        IPL-1.0 OR EPL-2.0
URL:            https://www.postfix.org/
# VCS: No VCS link available
#!RemoteAsset:  sha256:4a6ab3d0e9390989fa201fc6c446045fc702c4e16e7a247c3ae261c9e9bee610
Source0:        http://ftp.porcupine.org/mirrors/postfix-release/official/postfix-%{version}.tar.gz
Source1:        postfix.service
Source2:        postfix.sysusers
BuildSystem:    autotools

BuildOption(build):  -f Makefile.init
BuildOption(build):  update
BuildOption(build):  pie=yes
BuildOption(build):  shared=no
BuildOption(build):  dynamicmaps=no
BuildOption(build):  default_database_type=lmdb
BuildOption(build):  default_cache_db_type=lmdb
BuildOption(build):  config_directory=%{postfix_config_dir}
BuildOption(build):  CCARGS="-DNO_DB -DNO_NIS -DHAS_LDAP -DLDAP_DEPRECATED=1 -DUSE_LDAP_SASL -I%{_includedir}/sasl -DHAS_LMDB -DHAS_PCRE=2 $(pkg-config --cflags libpcre2-8) -DHAS_MYSQL $(pkg-config --cflags libmariadb) -DHAS_PGSQL $(pkg-config --cflags libpq) -DHAS_SQLITE $(pkg-config --cflags sqlite3) -DUSE_SASL_AUTH -DUSE_CYRUS_SASL $(pkg-config --cflags libsasl2) -DUSE_TLS $(pkg-config --cflags openssl)"
BuildOption(build):  AUXLIBS="$(pkg-config --libs libsasl2 openssl)"
BuildOption(build):  AUXLIBS_LDAP="$(pkg-config --libs ldap)"
BuildOption(build):  AUXLIBS_LMDB="$(pkg-config --libs lmdb)"
BuildOption(build):  AUXLIBS_PCRE="$(pkg-config --libs libpcre2-8)"
BuildOption(build):  AUXLIBS_MYSQL="$(pkg-config --libs libmariadb)"
BuildOption(build):  AUXLIBS_PGSQL="$(pkg-config --libs libpq)"
BuildOption(build):  AUXLIBS_SQLITE="$(pkg-config --libs sqlite3)"
BuildOption(build):  OPT="%{build_cflags} -fno-strict-aliasing"
BuildOption(build):  DEBUG=""
BuildOption(build):  POSTFIX_INSTALL_OPTS=-keep-build-mtime

BuildRequires:  make
BuildRequires:  m4
BuildRequires:  pkgconfig(icu-uc)
BuildRequires:  pkgconfig(ldap)
BuildRequires:  pkgconfig(libmariadb)
BuildRequires:  pkgconfig(libpcre2-8)
BuildRequires:  pkgconfig(libpq)
BuildRequires:  pkgconfig(libsasl2)
BuildRequires:  pkgconfig(lmdb)
BuildRequires:  pkgconfig(openssl)
BuildRequires:  pkgconfig(sqlite3)
BuildRequires:  systemd-rpm-macros

Requires:       diffutils
Requires:       findutils
Requires(pre):  systemd-sysusers
Requires(post):  update-alternatives
Requires(postun):  update-alternatives
%systemd_requires

Provides:       MTA
Provides:       smtpdaemon

%description
Postfix is a mail transport agent that routes and delivers electronic mail.
It supports SMTP, TLS, SASL, LDAP, SQL, LMDB, and PCRE lookup tables.

%conf
# Postfix has no configure script; Makefile.init generates its makefiles.

%install
make non-interactive-package \
    install_root=%{buildroot} \
    config_directory=%{postfix_config_dir} \
    meta_directory=%{postfix_config_dir} \
    daemon_directory=%{postfix_daemon_dir} \
    command_directory=%{_sbindir} \
    queue_directory=%{postfix_queue_dir} \
    data_directory=%{postfix_data_dir} \
    sendmail_path=%{_sbindir}/sendmail.postfix \
    newaliases_path=%{_bindir}/newaliases.postfix \
    mailq_path=%{_bindir}/mailq.postfix \
    mail_owner=%{postfix_user} \
    setgid_group=%{postdrop_group} \
    manpage_directory=%{_mandir}

for manpage in man1/mailq.1 man1/newaliases.1 man1/sendmail.1 \
    man5/aliases.5 man8/smtp.8 man8/smtpd.8; do
    postfix_manpage="${manpage%.*}.postfix.${manpage##*.}"
    mv "%{buildroot}%{_mandir}/$manpage" \
        "%{buildroot}%{_mandir}/$postfix_manpage"
    sed -i "s|^\\.so $manpage$|.so $postfix_manpage|" \
        %{buildroot}%{_mandir}/man?/*.[1-9]
    sed -i "s|/$manpage:|/$postfix_manpage:|" \
        %{buildroot}%{postfix_config_dir}/postfix-files
done

install -D -m 0644 %{SOURCE1} %{buildroot}%{_unitdir}/postfix.service
install -D -m 0644 %{SOURCE2} %{buildroot}%{_sysusersdir}/postfix.conf

sed -E -i \
    -e '\#^\$config_directory/(TLS_)?LICENSE:#d' \
    -e '\#^\$(html|manpage|readme|sample)_directory[:/]#d' \
    %{buildroot}%{postfix_config_dir}/postfix-files
if grep -Eq '^\$config_directory/(TLS_)?LICENSE:|^\$(html|manpage|readme|sample)_directory[:/]' \
    %{buildroot}%{postfix_config_dir}/postfix-files; then
    exit 1
fi
rm -f %{buildroot}%{postfix_config_dir}/{LICENSE,TLS_LICENSE}

%check
# Postfix does not provide a check target.

%pre
%sysusers_create_package %{name} %{SOURCE2}

%post
%systemd_post postfix.service

if [ "$1" -eq 1 ]; then
    postfix_post_install_action=set-permissions
else
    postfix_post_install_action=upgrade-package
fi

%{postfix_daemon_dir}/post-install \
    config_directory=%{postfix_config_dir} \
    meta_directory=%{postfix_config_dir} \
    daemon_directory=%{postfix_daemon_dir} \
    command_directory=%{_sbindir} \
    queue_directory=%{postfix_queue_dir} \
    data_directory=%{postfix_data_dir} \
    mail_owner=%{postfix_user} \
    setgid_group=%{postdrop_group} \
    manpage_directory=%{_mandir} \
    "$postfix_post_install_action" || exit 1

update-alternatives --install \
    /usr/sbin/sendmail mta %{_sbindir}/sendmail.postfix 60 \
    --slave %{_bindir}/mailq mta-mailq %{_bindir}/mailq.postfix \
    --slave %{_bindir}/newaliases mta-newaliases %{_bindir}/newaliases.postfix \
    --slave %{_mandir}/man1/mailq.1.gz mta-mailqman %{_mandir}/man1/mailq.postfix.1.gz \
    --slave %{_mandir}/man1/newaliases.1.gz mta-newaliasesman %{_mandir}/man1/newaliases.postfix.1.gz \
    --slave %{_mandir}/man8/sendmail.8.gz mta-sendmailman %{_mandir}/man1/sendmail.postfix.1.gz \
    --slave %{_mandir}/man5/aliases.5.gz mta-aliasesman %{_mandir}/man5/aliases.postfix.5.gz \
    --slave %{_mandir}/man8/smtp.8.gz mta-smtpman %{_mandir}/man8/smtp.postfix.8.gz \
    --slave %{_mandir}/man8/smtpd.8.gz mta-smtpdman %{_mandir}/man8/smtpd.postfix.8.gz \
    >/dev/null || exit 1

%preun
%systemd_preun postfix.service

%postun
%systemd_postun_with_restart postfix.service

if [ "$1" -eq 0 ]; then
    mta_current=$(readlink %{_sysconfdir}/alternatives/mta 2>/dev/null || :)
    update-alternatives --remove mta %{_sbindir}/sendmail.postfix \
        >/dev/null 2>&1 || :
    if [ -n "$mta_current" ] &&
        [ "$mta_current" != "%{_sbindir}/sendmail.postfix" ]; then
        update-alternatives --set mta "$mta_current" \
            >/dev/null 2>&1 || :
    fi
fi

%files
%doc COMPATIBILITY HISTORY README_FILES RELEASE_NOTES TLS_ACKNOWLEDGEMENTS
%license LICENSE TLS_LICENSE
%dir %{postfix_config_dir}
%config(noreplace) %{postfix_config_dir}/access
%config(noreplace) %{postfix_config_dir}/aliases
%{postfix_config_dir}/bounce.cf.default
%config(noreplace) %{postfix_config_dir}/canonical
%config(noreplace) %{postfix_config_dir}/generic
%config(noreplace) %{postfix_config_dir}/header_checks
%config(noreplace) %{postfix_config_dir}/main.cf
%{postfix_config_dir}/main.cf.default
%{postfix_config_dir}/main.cf.proto
%{postfix_config_dir}/makedefs.out
%config(noreplace) %{postfix_config_dir}/master.cf
%{postfix_config_dir}/master.cf.proto
%{postfix_config_dir}/postfix-files
%dir %{postfix_config_dir}/postfix-files.d
%config(noreplace) %{postfix_config_dir}/relocated
%config(noreplace) %{postfix_config_dir}/transport
%config(noreplace) %{postfix_config_dir}/virtual
%{_bindir}/mailq.postfix
%{_bindir}/newaliases.postfix
%{_sbindir}/postalias
%{_sbindir}/postcat
%{_sbindir}/postconf
%attr(2755, root, %{postdrop_group}) %{_sbindir}/postdrop
%{_sbindir}/postfix
%{_sbindir}/postkick
%{_sbindir}/postlock
%attr(2755, root, %{postdrop_group}) %{_sbindir}/postlog
%{_sbindir}/postmap
%{_sbindir}/postmulti
%attr(2755, root, %{postdrop_group}) %{_sbindir}/postqueue
%{_sbindir}/postsuper
%{_sbindir}/sendmail.postfix
%{postfix_daemon_dir}
%{_mandir}/man1/*
%{_mandir}/man5/*
%{_mandir}/man8/*
%{_unitdir}/postfix.service
%{_sysusersdir}/postfix.conf
%ghost /usr/sbin/sendmail
%ghost %{_bindir}/mailq
%ghost %{_bindir}/newaliases
%ghost %{_mandir}/man1/mailq.1.gz
%ghost %{_mandir}/man1/newaliases.1.gz
%ghost %{_mandir}/man5/aliases.5.gz
%ghost %{_mandir}/man8/sendmail.8.gz
%ghost %{_mandir}/man8/smtp.8.gz
%ghost %{_mandir}/man8/smtpd.8.gz
%ghost %dir %attr(0700, %{postfix_user}, root) %{postfix_data_dir}
%ghost %dir %{postfix_queue_dir}

%changelog
%autochangelog
