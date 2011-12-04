Name: hunspell-kk
Summary: Kazakh hunspell dictionaries
Version: 1.1
Release: 1.1%{?dist}
Group: Applications/Text
Source: http://extensions.services.openoffice.org/files/1172/8/dict-kk.zip
URL: http://extensions.services.openoffice.org/project/dict-kk
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
License: GPLv2+ or LGPLv2+ or MPLv1.1
BuildArch: noarch

Requires: hunspell

%description
Kazakh hunspell dictionaries.

%prep
%setup -q -c -n hunspell-kk

%build
for i in README_kk_KZ.txt; do
  tr -d '\r' < $i > $i.new
  touch -r $i $i.new
  mv -f $i.new $i
done

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/%{_datadir}/myspell
cp -p kk_KZ.* $RPM_BUILD_ROOT/%{_datadir}/myspell

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%doc README_kk_KZ.txt
%{_datadir}/myspell/*

%changelog
* Mon Nov 30 2009 Dennis Gregorovic <dgregor@redhat.com> - 1.1-1.1
- Rebuilt for RHEL 6

* Wed Aug 26 2009 Caolan McNamara <caolanm@redhat.com> - 1.1-1
- latest version

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Sat Jul 11 2009 Caolan McNamara <caolanm@redhat.com> - 1.0-2
- tidy spec

* Mon Apr 20 2009 Caolan McNamara <caolanm@redhat.com> - 1.0-1
- initial version
