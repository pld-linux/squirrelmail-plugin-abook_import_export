%define		_plugin	abook_import_export
%define		mversion	1.4.4
Summary:	A squirrel LDIF Address Book Import plug-in
Name:		squirrelmail-plugin-%{_plugin}
Version:	1.0
Release:	1
License:	GPL v2
Group:		Applications/Mail
Source0:	http://www.squirrelmail.org/plugins/%{_plugin}-%{version}-%{mversion}.tar.gz
# Source0-md5:	48098d57e81df8ea71e33351b51c1938
URL:		http://www.squirrelmail.org/plugin_view.php?id=29
Requires:	squirrelmail >= 1.4.4
Requires:	squirrelmail-compatibility-2.0.4
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_plugindir	%{_datadir}/squirrelmail/plugins/%{_plugin}
%define		_sysconfdir	/etc/webapps/squirrelmail

%description
Allows for the importing of addressbooks from a CSV (comma separated values)
file. This will be located at the bottom of the "Addresses" section.

%prep
%setup -q -n %{_plugin}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_plugindir} $RPM_BUILD_ROOT%{_sysconfdir}

mv config_default.php $RPM_BUILD_ROOT%{_sysconfdir}/%{_plugin}_config.php
install *.php $RPM_BUILD_ROOT%{_plugindir}
ln -s %{_sysconfdir}/%{_plugin}_config.php $RPM_BUILD_ROOT%{_plugindir}/config.php

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc CHANGELOG README ReleaseNotes.txt
%attr(640,root,http) %config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/%{_plugin}_config.php
%dir %{_plugindir}
%{_plugindir}/*.php